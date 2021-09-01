# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
import json

from jsonpath import jsonpath

from test_wework.api.tag import Tag


class TestTag:
    def setup(self):
        self.tag = Tag()

    def test_all(self):
        tagId = jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="yyaa")].id')
        if tagId:
            self.tag.delete_tag(tagId[0])

        self.tag.add_tag("yyaa-1")

        tag_Id = jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="yyaa-1")].id')[0]
        self.tag.update_tag(tag_Id, "yyaa")

    def test_add_tag(self):
        print(Tag().add_tag("opp"))

    def test_get_tag(self):
        print(json.dumps(Tag().get_tag(), indent=2))

    def test_delete_tag(self):
        tagId = jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="opp")].id')[0]
        print(Tag().delete_tag(tagId))

    def test_update_tag(self):
        self.tag.add_tag("oppa")
        tagId = jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="oppa")].id')[0]
        print(Tag().update_tag(tagId, "oppoo"))
