#!/usr/bin/env python

"""
Each config value will be automatically converted to one of the following types, based on the suffix of the variable's name:

   '_INT'     = integer
   '_FLOAT'   = float
   '_JSON'    = JSON
   '_FJSON'   = JSON loaded from filename.
      *       = string

See `mediachain.indexer.mc_generic.config_env` for more details on parsing of this config.

Config structure in `mediachain.indexer.mc_config`:

   {'section_title':{var_name:(var_value,'var_description')}}

   or

   {'section_title':{var_name:(var_value,['var_description', 'more_description'])}}

"""

LOW_LEVEL = True ## Temporary - For transitioning from old approach to new.


cfg = {'1. Model Settings. NOTE - WIP. These settings are not enabled yet.':
           {'MC_MODELS_JSON':('{"model_1":{"descriptors":{"name":"VectorsBaseline"},"neighbors":{"name":"ElasticSearchNN"},"rerank":{"name":"ReRankBasic"}}}',
                             'JSON hyper-parameter settings for each model that should be trained.'
                             ),
            'MC_MODELS_FJSON':(None,
                              'This overrides `MC_MODEL_JSON`. Pass path to JSON file containing `MC_MODEL_JSON` settings.'
                              ),
            },
       '2. Elasticsearch Settings':
           {'MC_ES_URLS':('',
                          ['One or more comma-separated RFC-1738 formatted URLs.',
                           '\ne.g. "http://user:secret@localhost:9200/,https://user:secret@other_host:443/production"']
                          ),
            'MC_NUMBER_OF_SHARDS_INT':('1', ''),
            'MC_NUMBER_OF_REPLICAS_INT':('0', ''),
            'MC_INDEX_NAME':('getty_test', ''),
            'MC_DOC_TYPE':('image', ''),
           },
       '3. Ingestion Settings':
           {'MC_GETTY_KEY':('', 'Getty key, for creating local dump of getty images'),
            'MC_DATASTORE_HOST': ('facade.mediachain.io', 'Datastore host.'),
            'MC_DATASTORE_PORT_INT': ('10002', 'Datastore port.'),
            'MC_IPFS_URL': ('localhost', 'IPFS host.'),
            'MC_IPFS_PORT_INT': ('5001', 'IPFS port.'),
            'MC_USE_IPFS_INT':(1, 'Use IPFS for image ingestion.'),
           },
       '4. REST API Settings':
           {'MC_QUERY_CACHE_DIR':('/datasets/datasets/query_cache/', 'Location of where to store query cache.'),
            'MC_IMAGE_CACHE_DIR':('/datasets/datasets/indexer_cache/images/', 'Location of where to store cached images, for serving to frontend.'),
            'MC_IMAGE_CACHE_HOST':('http://api.mediachain.io/images/', 'Image host, for serving cached images to frontend.'),
            'MC_ALLOW_SKIP_QUERY_CACHE_INT':('1', 'Allow Indexer `skip_cache` arg.'),
            'MC_FILTER_INCOMPLETE_INT':('0', ["Temporary - ",
                                              "Set to \"1\" filter out image results for which we don't have a high-res image. ",
                                              "Currently, we set to \"1\" if the Indexer is being used with the Frontend.",
                                              ]),
            },
       '5. Settings for Automated Tests':
           {'MC_TEST_WEB_HOST':('http://127.0.0.1:23456', ''),
            'MC_TEST_INDEX_NAME':('mc_test', ''),
            'MC_TEST_DOC_TYPE':('mc_test_image', 'Document type, required for some neighbors models.'),
           },
       '6. Transactor Settings':
           {'MC_TRANSACTOR_HOST':('facade.mediachain.io', 'Mediachain transactor RPC host.'),
            'MC_TRANSACTOR_PORT_INT':('10001', ''),
           },
       }

import mc_generic
mc_generic.config_env(cfg, globals())


