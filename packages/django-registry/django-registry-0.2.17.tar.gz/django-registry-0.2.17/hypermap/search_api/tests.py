import json
import requests
import time
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from hypermap.aggregator.models import Catalog
from hypermap.search_api import utils
from hypermap.aggregator.solr import SolrHypermap


SEARCH_URL = settings.REGISTRY_SEARCH_URL.split('+')[1]


class SearchApiTestCase(TestCase):
    """
    run me
    python manage.py test hypermap.search_api --settings=hypermap.settings.test --failfast
    """

    def setUp(self):
        self.solr = SolrHypermap()
        catalog_test_slug = "hypermap"
        self.url_solr_update = '{0}/solr/{1}/update/json/docs'.format(
            SEARCH_URL, catalog_test_slug
        )
        self.url_solr_search = '{0}/solr/{1}/select'.format(
            SEARCH_URL, catalog_test_slug
        )
        self.api_url = "{0}{1}".format(
            settings.SITE_URL, reverse("search_api", args=[catalog_test_slug])
        )

        Catalog.objects.get_or_create(
            name=catalog_test_slug
        )

        # delete solr documents
        print '> clearing SEARCH_URL={0}'.format(SEARCH_URL)
        self.solr.clear_solr(catalog=catalog_test_slug)

        # add test solr documents
        self.solr_records = [
            {
                "abstract": "Downtown-New-Orleans-Map ",
                "layer_originator": "warp.worldmap.harvard.edu",
                "availability": "Online",
                "min_x": -40.0,
                "max_x": -20.0,
                "max_y": -20.0,
                "min_y": -40.0,
                "bbox": "ENVELOPE(-40.0,-20.0,-20.0,-40.0)",
                "title": "1",
                "domain_name": "warp.worldmap.harvard.edu",
                "id": 1,
                "location": "{\"layerInfoPage\": \"/layer/998/\"}",
                "service_type": "Hypermap:WARPER",
                "layer_datetype": "From Metadata",
                "layer_id": 1,
                "is_public": True,
                "layer_date": "2000-03-01T00:00:00Z",
                "name": "1490",
                "url": "http://warp.worldmap.harvard.edu/maps/wms/1490?",
                "type": "Layer",
                "area": 1,
                "tile_url": "/layers/998/map/wmts/nypl_map/default_grid/{z}/{y}/{x}.png",
                "srs": ["EPSG:3857",
                        "EPSG:900913",
                        "EPSG:4326"],
                "layer_username": "xxx",
                "layer_category": "xxx",
                "centroid_y": 1,
                "centroid_x": 1,
            },
            {
                "abstract": "Downtown-New-Orleans-Map ",
                "layer_originator": "warp.worldmap.harvard.edu",
                "availability": "Online",
                "min_x": -40,
                "max_x": -20,
                "max_y": 40,
                "min_y": 20,
                "bbox": "ENVELOPE(-40,-20,40,20)",
                "title": "20",
                "domain_name": "warp.worldmap.harvard.edu",
                "id": 2,
                "location": "{\"layerInfoPage\": \"/layer/998/\"}",
                "service_type": "Hypermap:WARPER",
                "layer_datetype": "From Metadata",
                "layer_id": 2,

                "is_public": True,
                "layer_date": "2001-03-01T00:00:00Z",
                "name": "1490",
                "url": "http://warp.worldmap.harvard.edu/maps/wms/1490?",
                "type": "Layer",
                "area": 2,
                "tile_url": "/layers/998/map/wmts/nypl_map/default_grid/{z}/{y}/{x}.png",
                "srs": ["EPSG:3857",
                        "EPSG:900913",
                        "EPSG:4326"],
                "service_id": 2
            },
            {
                "abstract": "Downtown-New-Orleans-Map ",
                "layer_originator": "warp.worldmap.harvard.edu",
                "availability": "Online",
                "min_x": 20,
                "max_x": 40,
                "max_y": 40,
                "min_y": 20,
                "bbox": "ENVELOPE(20,40,40,20)",
                "title": "3",
                "domain_name": "warp.worldmap.harvard.edu",
                "id": 3,
                "location": "{\"layerInfoPage\": \"/layer/998/\"}",
                "service_type": "Hypermap:WARPER",
                "layer_datetype": "From Metadata",
                "layer_id": 30,
                "is_public": True,
                "layer_date": "2002-03-01T00:00:00Z",
                "name": "1490",
                "url": "http://warp.worldmap.harvard.edu/maps/wms/1490?",
                "type": "Layer",
                "area": 3,
                "tile_url": "/layers/998/map/wmts/nypl_map/default_grid/{z}/{y}/{x}.png",
                "srs": ["EPSG:3857",
                        "EPSG:900913",
                        "EPSG:4326"],
                "service_id": 3
            },
            {
                "abstract": "Downtown-New-Orleans-Map ",
                "layer_originator": "warp.worldmap.harvard.edu",
                "availability": "Online",
                "min_x": 20,
                "max_x": 40,
                "max_y": -20,
                "min_y": -40,
                "bbox": "ENVELOPE(20,40,-20,-40)",
                "title": "Layer with a BCE date",
                "domain_name": "warp.worldmap.harvard.edu",
                "id": 4,
                "location": "{\"layerInfoPage\": \"/layer/998/\"}",
                "service_type": "Hypermap:WARPER",
                "layer_datetype": "From Metadata",
                "layer_id": 4,
                "is_public": True,
                "layer_date": "-5000000-01-01T00:00:00Z",
                "name": "1490",
                "url": "http://warp.worldmap.harvard.edu/maps/wms/1490?",
                "type": "Layer",
                "area": 4,
                "tile_url": "/layers/998/map/wmts/nypl_map/default_grid/{z}/{y}/{x}.png",
                "srs": ["EPSG:3857",
                        "EPSG:900913",
                        "EPSG:4326"],
                "service_id": 4
            }

        ]

        # add the schema
        self.solr.update_schema(catalog=catalog_test_slug)

        headers = {"content-type": "application/json"}
        params = {"commitWithin": 1500}
        solr_json = json.dumps(self.solr_records)
        print '> Sending layers to Solr [SEARCH_URL={0}]'.format(SEARCH_URL)
        post_layers = requests.post(self.url_solr_update, data=solr_json, params=params, headers=headers)
        print post_layers.text
        self.assertFalse('error' in post_layers.json())

        # solr have commitWithin 1500.
        # before to proceed with the tests wait for 2 secs.
        # otherwise it will return zero docs in the next test.
        time.sleep(2)
        # TODO: deeper tests: index with SolrHypermap.layer_to_solr(aggregator.models.Layer)

        self.default_params = {
            "search_engine": "solr",
            "search_engine_endpoint": self.url_solr_search,
            "q_time": "[* TO *]",
            "q_geo": "[-90,-180 TO 90,180]",
            "d_docs_limit": 0,
            "d_docs_page": 1,
            "d_docs_sort": "score"
        }

    def test_catalogs(self):
        print '> testing catalogs'
        url = settings.SITE_URL + reverse("catalog-list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        catalogs = json.loads(res.content)
        self.assertEqual(len(catalogs), 1)

    def test_all_match_docs(self):
        print '> testing match all docs'
        params = self.default_params
        print "searching on [{}]".format(self.api_url)
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        self.assertEqual(results["a.matchDocs"], len(self.solr_records))

    def test_q_text(self):
        print '> testing q text'
        params = self.default_params
        params["q_text"] = "title:1"
        params["d_docs_limit"] = 100

        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)

        results = json.loads(results.content)
        self.assertEqual(results["a.matchDocs"], 1)

        for doc in results.get("d.docs", []):
            self.assertEqual(doc["title"], "1")

    def test_q_time(self):
        print '> testing q time (format validations)'
        params = self.default_params

        # test validations
        params["q_time"] = "[2000-01-01 - 2001-01-01T00:00:00]"
        results = self.client.get(self.api_url, params)
        # requires [X TO Y]
        self.assertEqual(400, results.status_code)

        print '> testing q time'
        # test asterisks
        # all times
        params["q_time"] = "[* TO *]"
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        # all records
        self.assertEqual(results["a.matchDocs"], len(self.solr_records))

        # test range
        # entire year 2000
        params["q_time"] = "[2000-01-01 TO 2001-01-01T00:00:00]"
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        # 1 in year 2000
        self.assertEqual(results["a.matchDocs"], 1)

        # test complete min and max when q time is asterisks
        params["q_time"] = "[* TO *]"
        params["a_time_limit"] = 1
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        self.assertEqual(results["a.matchDocs"], len(self.solr_records))
        # * to first date
        self.assertEqual(results["a.time"]["start"], "-5000000-01-01T00:00:00Z")
        # TODO: returning "2100-01-01T00:00:00Z" because BCE dates cant calculate time duration.
        # self.assertEqual(results["a.time"]["end"], "2002-03-01T00:00:00Z") # * to last date

        # test facets
        params["q_time"] = "[2000 TO 2022]"
        params["a_time_limit"] = 1
        params["a_time_gap"] = "P1Y"
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        self.assertEqual(results["a.matchDocs"], 3)
        # 2000 to complete datetime format
        self.assertEqual(results["a.time"]["start"], "2000-01-01T00:00:00Z")
        # 2022 to complete datetime format
        self.assertEqual(results["a.time"]["end"], "2022-01-01T00:00:00Z")
        # the facet counters are all facets excluding < 2000
        self.assertEqual(len(results["a.time"]["counts"]), 3)

    def test_q_geo(self):
        print '> testing q geo'
        params = self.default_params

        # top right square
        params["q_geo"] = "[0,0 TO 30,30]"
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        self.assertEqual(results["a.matchDocs"], 1)

        # bottom left square
        params["q_geo"] = "[-30,-30 TO 0,0]"
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        self.assertEqual(results["a.matchDocs"], 1)

        # big square
        params["q_geo"] = "[-30,-30 TO 30,30]"
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        self.assertEqual(results["a.matchDocs"], 4)

        # center where no layers
        params["q_geo"] = "[-5,-5 TO 5,5]"
        results = self.client.get(self.api_url, params)
        self.assertEqual(results.status_code, 200)
        results = json.loads(results.content)
        self.assertEqual(results["a.matchDocs"], 0)

        # bad format
        params["q_geo"] = "[-5,-5 5,5]"
        results = self.client.get(self.api_url, params)
        # validate the format
        print '> testing q geo (format validations)'
        self.assertEqual(results.status_code, 400)

    def test_utilities(self):
        print '> testing utilities functions'
        # test_parse_datetime_range
        start, end = utils.parse_datetime_range("[2013-03-01 TO 2014-05-02T23:00:00]")
        self.assertTrue(start.get("is_common_era"))
        self.assertEqual(start.get("parsed_datetime").year, 2013)
        self.assertEqual(start.get("parsed_datetime").month, 3)
        self.assertEqual(start.get("parsed_datetime").day, 1)
        self.assertTrue(end.get("is_common_era"))
        self.assertEqual(end.get("parsed_datetime").year, 2014)
        self.assertEqual(end.get("parsed_datetime").month, 5)
        self.assertEqual(end.get("parsed_datetime").day, 2)
        self.assertEqual(end.get("parsed_datetime").hour, 23)
        self.assertEqual(end.get("parsed_datetime").minute, 0)
        self.assertEqual(end.get("parsed_datetime").second, 0)

        start, end = utils.parse_datetime_range("[-500000000 TO 2014-05-02T23:00:00]")
        self.assertFalse(start.get("is_common_era"))
        self.assertEqual(start.get("parsed_datetime"), "-500000000-01-01T00:00:00Z")

        start, end = utils.parse_datetime_range("[* TO *]")
        self.assertTrue(start.get("is_common_era"))
        self.assertEqual(start.get("parsed_datetime"), None)
        self.assertEqual(end.get("parsed_datetime"), None)

        # test_parse_ISO8601
        quantity, units = utils.parse_ISO8601("P3D")
        self.assertEqual(quantity, 3)
        self.assertEqual(units[0], "DAYS")

        # test_gap_to_sorl
        value = utils.gap_to_sorl("P3D")
        self.assertEqual(value, "+3DAYS")

        # test_parse_geo_box
        value = utils.parse_geo_box("[-90,-180 TO 90,180]")
        self.assertEqual(value.bounds[0], -90)
        self.assertEqual(value.bounds[1], -180)
        self.assertEqual(value.bounds[2], 90)
        self.assertEqual(value.bounds[3], 180)

        # test_request_time_facet
        d = utils.request_time_facet("x", "[2000 TO 2014-01-02T11:12:13]", None, 1000)
        self.assertEqual(type(d), dict)
        self.assertEqual(d['f.x.facet.range.start'], '2000-01-01T00:00:00Z')
        self.assertEqual(d['f.x.facet.range.end'], '2014-01-02T11:12:13Z')
        self.assertEqual(d['f.x.facet.range.gap'], '+6DAYS')
        self.assertEqual(d['facet.range'], 'x')

        d = utils.request_time_facet("y", "[-5000000 TO 2016]", "P1D", 1)
        self.assertEqual(d['f.y.facet.range.start'], '-5000000-01-01T00:00:00Z')
        self.assertEqual(d['f.y.facet.range.end'], '2016-01-01T00:00:00Z')
        self.assertEqual(d['f.y.facet.range.gap'], '+1DAYS')
        self.assertEqual(d['facet.range'], 'y')
