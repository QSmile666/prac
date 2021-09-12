# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
import json

import allure
import pytest

from test_wework.api.tag import Tag


@allure.feature("企业标签")
class TestTag:
    tag = Tag()
    test_data = tag.load("test_tag_data.yaml")

    @classmethod
    def setup_class(cls):
        pass

    # 每个方法执行前都会执行一次
    def setup(self):
        pass

    @allure.story("企业标签的增删改查")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("name_old,name_new", test_data)
    def test_all(self, name_old, name_new):
        with allure.step("查询企业标签"):
            data = self.tag.get_tag()
        with allure.step("删除之前的企业标签"):
            for name in [name_old, name_new]:
                tag_id = self.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
                if tag_id:
                    self.tag.delete_tag(tag_id=tag_id[0])
        with allure.step("添加删除的同名的企业标签"):
            assert self.tag.add_tag(tag_name=name_old)["errcode"] == 0
        with allure.step("获取新创建的标签的tag_id"):
            tag_id = self.tag.jsonpath(self.tag.get_tag(), f'$..tag[?(@.name=="{name_old}")].id')[0]

        with allure.step("更新企业标签"):
            assert self.tag.update_tag(tag_id=tag_id, name=name_new)["errcode"] == 0

    @allure.story("添加企业标签")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_tag(self):
        assert self.tag.add_tag(tag_name="opp")["errcode"] == 0

    @allure.story("查询企业标签")
    def test_get_tag(self):
        assert self.tag.get_tag()["errcode"] == 0

    @allure.story("删除企业标签")
    def test_delete_tag(self):
        name = "opp"
        # assert self.tag.add_tag(tag_name=name)["errcode"] == 0
        tag_id = self.tag.jsonpath(self.tag.get_tag(), f'$..tag[?(@.name=="{name}")].id')[0]
        print(Tag().delete_tag(tag_id=tag_id))

    @allure.story("更新企业标签")
    def test_update_tag(self):
        self.tag.add_tag(tag_name="oppaa")
        tag_id = self.tag.jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="oppa")].id')[0]
        assert self.tag.update_tag(tag_id=tag_id, name="oppoo")
