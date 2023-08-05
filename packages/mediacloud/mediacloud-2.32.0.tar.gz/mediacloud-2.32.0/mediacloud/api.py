import logging
import datetime
from collections import namedtuple
import requests
import mediacloud, mediacloud.error

MAX_HTTP_GET_CHARS = 4000   # experimentally determined for our main servers (conservative)

class MediaCloud(object):
    '''
    Simple client library for the MediaCloud API v2
    '''

    V2_API_URL = "https://api.mediacloud.org/api/v2/"

    SORT_PUBLISH_DATE_ASC = "publish_date_asc"
    SORT_PUBLISH_DATE_DESC = "publish_date_desc"
    SORT_RANDOM = "random"

    MSG_CORE_NLP_NOT_ANNOTATED = "story is not annotated"

    SENTENCE_PUBLISH_DATE_FORMAT = "%Y-%m-%d %H:%M:%S" # use with datetime.datetime.strptime

    def __init__(self, auth_token=None, all_fields=False):
        self._logger = logging.getLogger(__name__)
        self.setAuthToken(auth_token)
        self.setAllFields(all_fields)

    def setAllFields(self, all_fields):
        '''
        Specify the value of the all_fields param to use for all future requests
        '''
        self._all_fields = all_fields

    def setAuthToken(self, auth_token):
        '''
        Specify the auth_token to use for all future requests
        '''
        self._auth_token = auth_token

    def userAuthToken(self, username, password):
        '''
        Get a auth_token for future requests to use
        '''
        self._logger.debug("Requesting new auth token for "+username)
        response = self._queryForJson(self.V2_API_URL+'auth/single/',
            {'username':username, 'password':password})
        response = response[0]
        if response['result'] == 'found':
            self._logger.debug(" new token is "+response['token'])
            return response['token']
        else:
            self._logger.warn("AuthToken request for "+username+" failed!")
            raise RuntimeError(response['result'])

    def verifyAuthToken(self):
        try:
            self.tagSetList(0, 1)
            return True
        except mediacloud.error.MCException:
            return False
        except Exception as exception:
            self._logger.warn("AuthToken verify failed: %s" % exception)
        return False

    def media(self, media_id):
        '''
        Details about one media source
        '''
        return self._queryForJson(self.V2_API_URL+'media/single/'+str(media_id))[0]

    def mediaHealth(self, media_id):
        '''
        Details about one media source
        '''
        return self._queryForJson(self.V2_API_URL+'mediahealth/list',
            {'media_id':media_id} )[0]

    def mediaList(self, last_media_id=0, rows=20, name_like=None,
                controversy_dump_time_slices_id=None, controversy_mode=None, tags_id=None, q=None):
        '''
        Page through all media sources
        '''
        params = {'last_media_id':last_media_id, 'rows':rows}
        if name_like is not None:
            params['name'] = name_like
        if controversy_dump_time_slices_id is not None:
            params['controversy_dump_time_slices_id'] = controversy_dump_time_slices_id
        if controversy_mode is not None:
            params['controversy_mode'] = controversy_mode
        if tags_id is not None:
            params['tags_id'] = tags_id
        if q is not None:
            params['q'] = q
        return self._queryForJson(self.V2_API_URL+'media/list', params)

    def feed(self, feeds_id):
        '''
        Details about one feed
        '''
        return self._queryForJson(self.V2_API_URL+'feeds/single/'+str(feeds_id))[0]

    def feedList(self, media_id, last_feeds_id=0, rows=20):
        '''
        Page through all the feeds of one media source
        '''
        return self._queryForJson(self.V2_API_URL+'feeds/list',
            {'media_id':media_id, 'last_feeds_id':last_feeds_id, 'rows':rows} )

    def storyPublic(self, stories_id):
        '''
        Maintained for backwards compatability
        '''
        return self.story(stories_id)

    def story(self, stories_id):
        '''
        Authenticated Public Users: Details about one story.
        Note that this does NOT include text, nor sentences (due to copyright limitations).
        '''
        return self._queryForJson(self.V2_API_URL+'stories_public/single/'+str(stories_id))[0]

    def storyCount(self, solr_query='', solr_filter=''):
        '''
        The call returns the number of stories returned by Solr for the specified query
        '''
        return self._queryForJson(self.V2_API_URL+'stories_public/count',
                {'q': solr_query,
                 'fq': solr_filter
                })

    def storyPublicList(self, solr_query='', solr_filter='', last_processed_stories_id=0, rows=20):
        '''
        Maintained for backwards compatability
        '''
        return self.storyList(solr_query, solr_filter, last_processed_stories_id, rows)

    def storyList(self, solr_query='', solr_filter='', last_processed_stories_id=0, rows=20):
        '''
        Authenticated Public Users: Search for stories and page through results
        '''
        return self._queryForJson(self.V2_API_URL+'stories_public/list',
                {'q': solr_query,
                 'fq': solr_filter,
                 'last_processed_stories_id': last_processed_stories_id,
                 'rows': rows
                })

    def storyCoreNlpList(self, story_id_list):
        '''
        The stories/corenlp call takes as many stories_id= parameters as you want to pass it,
        and it returns the corenlp for each.
        {stories_id => 1, corenlp => {<corenlp data> } }
        If no corenlp annotation is available for a given story, the json element for that story looks like:
        {stories_id => 1, corenlp => 'story is not annotated' }
        '''
        return self._queryForJson(self.V2_API_URL+'stories/corenlp',
            {'stories_id': story_id_list} )

    def storyWordMatrix(self, solr_query='', solr_filter='', rows=1000, max_words=None, stopword_length=None ):
        '''
        Helpful to feed term-document-matrix driven analyses, like TF-IDF.
        '''
        params = {'q':solr_query, 'fq':solr_filter}
        params['rows'] = rows
        if max_words is not None:
            params['max_words'] = max_words
        if stopword_length is not None:
            if stopword_length in ['tiny', 'short', 'long']:
                params['stopword_length'] = stopword_length
            else:
                raise ValueError('Error - stopword_length must be "tiny", "short" or "long"')
        return self._queryForJson(self.V2_API_URL+'stories_public/word_matrix/', params)

    def sentence(self, story_sentences_id):
        '''
        Return info about a single sentence
        '''
        return self._queryForJson(self.V2_API_URL+'sentences/single/'+str(story_sentences_id))[0]

    def sentenceCount(self, solr_query, solr_filter=' ', split=False, split_start_date=None, split_end_date=None, split_daily=False):
        params = {'q':solr_query, 'fq':solr_filter}
        params['split'] = 1 if split is True else 0
        params['split_daily'] = 1 if split_daily is True else 0
        if split is True:
            datetime.datetime.strptime(split_start_date, '%Y-%m-%d')    #will throw a ValueError if invalid
            datetime.datetime.strptime(split_end_date, '%Y-%m-%d')    #will throw a ValueError if invalid
            params['split_start_date'] = split_start_date
            params['split_end_date'] = split_end_date
        return self._queryForJson(self.V2_API_URL+'sentences/count', params)

    def sentenceFieldCount(self, solr_query, solr_filter=' ', sample_size=1000, include_stats=False, field='tags_id_story_sentences', tag_sets_id=None):
        '''
        Right now the fields supported are 'tags_id_stories' or 'tags_id_story_sentences'
        '''
        params = {'q':solr_query, 'fq':solr_filter, 'sample_size':sample_size, 'field':field}
        if tag_sets_id is not None:
            params['tag_sets_id'] = tag_sets_id
        params['include_stats'] = 1 if include_stats is True else 0
        return self._queryForJson(self.V2_API_URL+'sentences/field_count', params)

    def wordCount(self, solr_query, solr_filter='', languages='en', num_words=500, sample_size=1000, include_stopwords=False, include_stats=False):
        params = {
            'q': solr_query,
            'l': languages,
            'num_words': num_words,
            'sample_size': sample_size,
            'include_stopwords': 1 if include_stopwords is True else 0,
            'include_stats': 1 if include_stats is True else 0,
        }
        if len(solr_filter) > 0:
            params['fq'] = solr_filter
        return self._queryForJson(self.V2_API_URL+'wc/list', params)

    def tag(self, tags_id):
        '''
        Details about one tag
        '''
        return self._queryForJson(self.V2_API_URL+'tags/single/'+str(tags_id))[0]

    def tagList(self, tag_sets_id=None, last_tags_id=0, rows=20, public_only=False, name_like=None):
        '''
        List all the tags in one tag set
        '''
        params = {
            'last_tags_id': last_tags_id
            , 'rows': rows
            , 'public': 1 if public_only is True else 0
        }
        if tag_sets_id is not None:
            params['tag_sets_id'] = tag_sets_id
        if name_like is not None:
            params['search'] = name_like
        return self._queryForJson(self.V2_API_URL+'tags/list', params)

    def tagSet(self, tag_sets_id):
        '''
        Details about one tag set
        '''
        return self._queryForJson(self.V2_API_URL+'tag_sets/single/'+str(tag_sets_id))[0]

    def tagSetList(self, last_tag_sets_id=0, rows=20):
        '''
        List all the tag sets
        '''
        return self._queryForJson(self.V2_API_URL+'tag_sets/list',
            {'last_tag_sets_id': last_tag_sets_id, 'rows':rows})

    def controversyDump(self, controversy_dumps_id):
        '''
        Details about one controversy dump
        '''
        return self._queryForJson(self.V2_API_URL+'controversy_dumps/single/'+str(controversy_dumps_id))[0]

    def controversyDumpTimeSlice(self, controversy_dump_time_slices_id):
        '''
        Details about one controversy dump time slice
        '''
        return self._queryForJson(self.V2_API_URL+'controversy_dump_time_slices/single/'+str(controversy_dump_time_slices_id))[0]

    def _queryForJson(self, url, params={}, http_method='GET'):
        '''
        Helper that returns queries to the API as real objects
        '''
        response = self._query(url, params, http_method)
        # print response.content
        response_json = response.json()
        # print json.dumps(response_json, indent=2)
        if 'error' in response_json:
            self._logger.error('Error in response from server on request to '+url+' : '+response_json['error'])
            raise mediacloud.error.MCException(response_json['error'], requests.codes.ok)
        return response_json

    def _query(self, url, params={}, http_method='GET'):
        self._logger.debug("query "+http_method+" to "+url+" with "+str(params))
        if not isinstance(params, dict):
            raise ValueError('Queries must include a dict of parameters')
        if 'key' not in params:
            params['key'] = self._auth_token
        if self._all_fields:
            params['all_fields'] = 1
        if http_method is 'GET':
            # switch to POST if request too long
            total_url_length = len(url)+sum([len(str(k)) for k in params.keys()])+sum([len(str(v)) for v in params.values()])
            try:
                if total_url_length > MAX_HTTP_GET_CHARS:
                    r = requests.post(url, data=params, headers={'Accept': 'application/json'} )
                else :
                    r = requests.get(url, params=params, headers={'Accept': 'application/json'} )
            except Exception as e:
                self._logger.error('Failed to GET or POST to url '+url+' because '+str(e))
                raise e
        elif http_method is 'PUT':
            try:
                r = requests.put( url, params=params, headers={'Accept': 'application/json'} )
            except Exception as e:
                self._logger.error('Failed to PUT url '+url+' because '+str(e))
                raise e
        else:
            raise ValueError('Error - unsupported HTTP method %s' % http_method)
        if r.status_code is not requests.codes.ok:
            self._logger.error('Bad HTTP response to '+r.url +' : '+str(r.status_code)  + ' ' +  str( r.reason) )
            self._logger.error('\t' + r.content )
            msg = 'Error - got a HTTP status code of %s with the message "%s", body: %s' % (
                str(r.status_code) , str(r.reason), str(r.text) )
            raise mediacloud.error.MCException(msg, r.status_code)
        return r

    def _zi_time(self, d):
        return datetime.datetime.combine(d, datetime.time.min).isoformat() + "Z"

    def _solr_date_range( self, start_date, end_date, start_date_inclusive=True, end_date_inclusive=False):
        ret = ''

        if start_date_inclusive:
            ret += '['
        else:
            ret += '{'

        ret += self._zi_time( start_date )

        ret += " TO "

        ret += self._zi_time( end_date )

        if end_date_inclusive:
            ret += ']'
        else:
            ret += '}'

        return ret

    def publish_date_query( self, start_date, end_date, start_date_inclusive=True, end_date_inclusive=False):
        return 'publish_date:' + self._solr_date_range( start_date, end_date, start_date_inclusive, end_date_inclusive)

# used when calling AdminMediaCloud.tagStories
StoryTag = namedtuple('StoryTag', ['stories_id', 'tag_set_name', 'tag_name'])

# used when calling AdminMediaCloud.tagSentences
SentenceTag = namedtuple('SentenceTag', ['story_sentences_id', 'tag_set_name', 'tag_name'])

class AdminMediaCloud(MediaCloud):
    '''
    A MediaCloud API client that includes admin-only methods, including to writing back
    data to MediaCloud.
    '''

    def story(self, stories_id, raw_1st_download=False, corenlp=False, sentences=False, text=False):
        '''
        Full details about one story.  Handy shortcut to storyList if you want sentences broken out
        '''
        return self._queryForJson(self.V2_API_URL+'stories/single/'+str(stories_id),
                {'raw_1st_download': 1 if raw_1st_download else 0,
                 'corenlp': 1 if corenlp else 0,
                 'sentences': 1 if sentences else 0,
                 'text': 1 if text else 0
                })[0]

    def storyList(self, solr_query='', solr_filter='', last_processed_stories_id=0, rows=20,
                  raw_1st_download=False, corenlp=False, sentences=False, text=False, ap_stories_id=0):
        '''
        Search for stories and page through results
        '''
        return self._queryForJson(self.V2_API_URL+'stories/list',
                {'q': solr_query,
                 'fq': solr_filter,
                 'last_processed_stories_id': last_processed_stories_id,
                 'rows': rows,
                 'raw_1st_download': 1 if raw_1st_download else 0,
                 'corenlp': 1 if corenlp else 0,    # this is slow - use storyCoreNlList instead
                 'sentences': 1 if sentences else 0,
                 'text': 1 if text else 0,
                 'ap_stories_id': 1 if ap_stories_id else 0
                })

    def sentenceList(self, solr_query, solr_filter='', start=0, rows=1000, sort=MediaCloud.SORT_PUBLISH_DATE_ASC):
        '''
        Search for sentences and page through results
        '''
        return self._queryForJson(self.V2_API_URL+'sentences/list',
                {'q': solr_query,
                 'fq': solr_filter,
                 'start': start,
                 'rows': rows,
                 'sort': sort
                })

    def tagStories(self, tags={}, clear_others=False):
        '''
        Add some tags to stories. The tags parameter should be a list of StoryTag objects
        Returns ["1, rahulb@media.mit.edu:example_tag_2"] as response
        '''
        params = {}
        if clear_others is True:
            params['clear_tags'] = 1
        custom_tags = []
        for tag in tags:
            if tag.__class__ is not StoryTag:
                raise ValueError('To use tagStories you must send in a list of StoryTag objects')
            custom_tags.append( '{}, {}:{}'.format( tag.stories_id, tag.tag_set_name, tag.tag_name ) )
        params['story_tag'] = custom_tags
        return self._queryForJson( self.V2_API_URL+'stories/put_tags', params, 'PUT')

    def tagSentences(self, tags={}, clear_others=False):
        '''
        Add some tags to sentences. The tags parameter should be a list of SentenceTag objects
        '''
        params = {}
        if clear_others is True:
            params['clear_tags'] = 1
        # bath into smaller requests so we don't hit the 414 Request-URI Too Large error
        results = []
        for tag_chunk in self._chunkify(tags, 50):
            custom_tags = []
            for tag in tag_chunk:
                if tag.__class__ is not SentenceTag:
                    raise ValueError('To use tagSentences you must send in a list of SentenceTag objects')
                custom_tags.append( '{}, {}:{}'.format( tag.story_sentences_id, tag.tag_set_name, tag.tag_name ) )
            params['sentence_tag'] = custom_tags
            results = results + self._queryForJson( self.V2_API_URL+'sentences/put_tags', params, 'PUT')
        return results

    def updateTag(self, tags_id, name, label, description):
        params = {}
        if name is not None:
            params['tag'] = name
        if label is not None:
            params['label'] = label
        if description is not None:
            params['description'] = description
        return self._queryForJson( (self.V2_API_URL+'tags/update/%d') % tags_id, params, 'PUT')

    def updateTagSet(self, tag_sets_id, name, label, description):
        params = {}
        if name is not None:
            params['name'] = name
        if label is not None:
            params['label'] = label
        if description is not None:
            params['description'] = description
        return self._queryForJson( (self.V2_API_URL+'tag_sets/update/%d') % tag_sets_id, params, 'PUT')

    def _chunkify(self, data, chunk_size):
        '''
        Helper method to break an array into a set of smaller arrays
        '''
        return [data[x:x+chunk_size] for x in xrange(0, len(data), chunk_size)]

    def topicMediaList(self, topic_id, snapshot_id=None, timespan_id=None, sort=None, limit=None, link_id=None):
        params = {}
        if sort is not None:
            if sort in ['social', 'inlink']:
                params['sort'] = sort
            else:
                raise ValueError('Sort must be either social or inlink')
        if snapshot_id is not None:
            params['snapshot'] = snapshot_id
        if timespan_id is not None:
            params['timeslice'] = timespan_id
        if limit is not None:
            params['limit'] = limit
        if link_id is not None:
            params['link_id'] = link_id
        return self._queryForJson(self.V2_API_URL+'topics/'+str(topic_id)+'/media/list', params)

    def topicStoryList(self, topic_id, snapshot_id=None, timespan_id=None, sort=None, limit=None, link_id=None):
        params = {'limit': limit}
        if sort is not None:
            if sort in ['social', 'inlink']:
                params['sort'] = sort
            else:
                raise ValueError('Sort must be either social or inlink')
        if snapshot_id is not None:
            params['snapshot'] = snapshot_id
        if timespan_id is not None:
            params['timeslice'] = timespan_id
        if limit is not None:
            params['limit'] = limit
        if link_id is not None:
            params['link_id'] = link_id
        return self._queryForJson(self.V2_API_URL+'topics/'+str(topic_id)+'/stories/list', params)

    def topicWordCount(self, topic_id, solr_query='*', solr_filter='', languages='en', num_words=500, sample_size=1000,
                        include_stopwords=False, snapshot_id=None, timespan_id=None, include_stats=False):
        params = {
            'q': solr_query,
            'l': languages,
            'num_words': num_words,
            'sample_size': sample_size,
            'include_stats': 1 if include_stats is True else 0,
            'include_stopwords': 1 if include_stopwords is True else 0
        }
        if snapshot_id is not None:
            params['snapshot'] = snapshot_id
        if timespan_id is not None:
            params['timeslice'] = timespan_id
        if len(solr_filter) > 0:
            params['fq'] = solr_filter
        return self._queryForJson(self.V2_API_URL+'topics/'+str(topic_id)+'/wc/list', params)

    def topicSentenceCount(self, topic_id, solr_query='*', solr_filter='',
        split=False, split_start_date=None, split_end_date=None, split_daily=False,
        snapshot_id=None, timespan_id=None ):
        params = {'q':solr_query, 'fq':solr_filter}
        params['split'] = 1 if split is True else 0
        params['split_daily'] = 1 if split_daily is True else 0
        if split is True:
            datetime.datetime.strptime(split_start_date, '%Y-%m-%d')    #will throw a ValueError if invalid
            datetime.datetime.strptime(split_end_date, '%Y-%m-%d')    #will throw a ValueError if invalid
            params['split_start_date'] = split_start_date
            params['split_end_date'] = split_end_date
        if snapshot_id is not None:
            params['snapshot'] = snapshot_id
        if timespan_id is not None:
            params['timeslice'] = timespan_id
        return self._queryForJson(self.V2_API_URL+'topics/'+str(topic_id)+'/sentences/count', params)

    def topic(self, topic_id):
        '''
        Details about one controversy
        '''
        return self._queryForJson(self.V2_API_URL+'topics/single/'+str(topic_id))[0]

    def topicList(self):
        '''
        List all the controversies
        '''
        return self._queryForJson(self.V2_API_URL+'topics/list')

    def topicSnapshotList(self, topic_id):
        '''
        List all the controversy dumps in a controversy
        '''
        return self._queryForJson(self.V2_API_URL+'topics/'+str(topic_id)+'/snapshots/list')['snapshots']

    def topicTimespanList(self, topic_id, snapshots_id=None, foci_id=None):
        '''
        List all the controversy dumps time slices in a controversy dump
        '''
        args = {}
        if snapshots_id is not None:
            args['snapshots_id'] = snapshots_id
        if foci_id is not None:
            args['foci_id'] = foci_id
        return self._queryForJson(self.V2_API_URL+'topics/'+str(topic_id)+'/timespans/list', args)['timespans']
