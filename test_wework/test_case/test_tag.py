# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
import json

import pytest

from test_wework.api.tag import Tag


class TestTag:
    tag = Tag()
    test_data = tag.load("test_tag_data.yaml")

    @classmethod
    def setup_class(cls):
        pass

    # 每个方法执行前都会执行一次
    def setup(self):
        pass

    @pytest.mark.parametrize("name_old,name_new", test_data)
    def test_all(self, name_old, name_new):
        data = self.tag.get_tag()

        for name in [name_old, name_new]:
            tag_id = self.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                self.tag.delete_tag(tag_id[0])

        assert self.tag.add_tag(name_old)["errcode"] == 0

        tag_id = self.tag.jsonpath(self.tag.get_tag(), f'$..tag[?(@.name=="{name_old}")].id')[0]
        assert self.tag.update_tag(tag_id, name_new)["errcode"] == 0

    def test_add_tag(self):
        assert self.tag.add_tag("opp")["errcode"] == 0

    def test_get_tag(self):
        assert json.dumps(self.tag.get_tag(), indent=2)["errcode"] == 0

    def test_delete_tag(self):
        tag_id = self.tag.jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="opp")].id')[0]
        assert self.tag.delete_tag(tag_id)

    def test_update_tag(self):
        self.tag.add_tag("oppa")
        tag_id = self.tag.jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="oppa")].id')[0]
        assert self.tag.update_tag(tag_id, "oppoo")
