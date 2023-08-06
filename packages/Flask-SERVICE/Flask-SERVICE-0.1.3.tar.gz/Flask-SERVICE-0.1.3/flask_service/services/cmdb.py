#coding:utf-8

import os
import json
import traceback
from base import BaseService

__author__ = 'lufeng'


class CMDBService(BaseService):
    """
    cmdb客户端链接工具
    """

    def get_email(self, um):
        emails = set([])
        result = self.get_resource("entity/search", {"schema": "user", "q": "attributes.um:%s" % um})
        if result.get("success"):
            for res in result["data"]["content"]:
                email = res.get("attributes", {}).get("email")
                for e in email:
                    if e:
                        emails.add(e)
        return list(emails)

    def get_department(self, um):
        """
        department
        :param um:
        :return:
        """
        if not um:
            return ''
        result = self.get_resource("entity/search", {"schema": "user", "q": "attributes.um:%s" % um})
        if result.get("success") and result["data"]["content"]:
            entity = result["data"]["content"][0]
            attr = entity.get("attributes", {})
            return attr.get("department", '')
        else:
            return ''

    def get_department_users(self, um):
        """
        获取部门用户列表
        :param um:
        :return:
        """
        users = set([])
        department = self.get_department(um)
        if not department:
            return list(users)
        result = self.get_resource("entity/search", {"schema": "user", "q": u"attributes.department:%s" % department})
        if result.get("success") and result["data"]["content"]:
            for ent in result["data"]["content"]:
                users.add(ent["attributes"]["um"])
        return list(users)

    def get_contact(self, um):
        """
        获取姓名和联系电话
        :param um:
        :return:
        """
        phone = set([])
        result = self.get_resource("entity/search", {"schema": "user", "q": "attributes.um:%s" % um})
        if result.get("success") and result["data"]["content"]:
            entity = result["data"]["content"][0]
            attr = entity.get("attributes", {})
            for p in attr.get("phone", []):
                if p:
                    phone.add(p)
            user = {
                "name": attr.get("name"),
                "phone": list(phone)
            }
            return user
        else:
            return None

    def get_name(self, um):
        """

        """
        if not um:
            return ''
        result = self.get_resource("entity/search", {"schema": "user", "q": "attributes.um:%s" % um})
        if result.get("success") and result["data"]["content"]:
            entity = result["data"]["content"][0]
            attr = entity.get("attributes", {})
            return attr.get("name", '')
        else:
            return ''

    def get_department_leader(self, um):
        """
        获取部门领导
        :param um:
        :return:
        """
        result = self.get_resource("entity/search", {"schema": "user", "q": "attributes.um:%s" % um})
        if result.get("success") and result["data"]["content"]:
            entity = result["data"]["content"][0]
            attr = entity.get("attributes", {})
            department = attr.get("department", '')
            if department:
                result = self.get_resource("entity/search", {"schema": "department", "q": "attributes.name:%s" % department})
                content = result["data"].get("content")
                if result.get("success") and content:
                    return content[0].get("attributes", {}).get("leader", "")
        else:
            return ''

    def get_team_leader(self, um):
        """
        获取组负责人
        :param um:
        :return:
        """
        result = self.get_resource("entity/search", {"schema": "user", "q": "attributes.um:%s" % um})
        if result.get("success") and result["data"]["content"]:
            entity = result["data"]["content"][0]
            attr = entity.get("attributes", {})
            team = attr.get("team", '')
            if team:
                result = self.get_resource("entity/search", {"schema": "team", "q": "attributes.name:%s" % team})
                content = result["data"].get("content")
                if result.get("success") and content:
                    return content[0].get("attributes", {}).get("leader", "")
        else:
            return ''

    def get_minions(self, um):
        """
        获取直接下属列表
        :param um:
        :return:
        """
        department = []
        team = []
        result = self.get_resource("entity/search", {"schema": ["department", "team"], "q": "attributes.leader:*\(%s\)*" % um})
        if result.get("success") and result["data"]["content"]:
            for entity in result["data"]["content"]:
                if entity["schema"] == "department":
                    department.append(entity["attributes"]["name"])
                else:
                    team.append(entity["attributes"]["name"])
        items = ["attributes.team:%s" % i for i in team]
        items.extend(["attributes.department:%s" % i for i in department])
        query = ' OR '.join(items)
        result = self.get_resource("entity/search", {"schema": "user", "q": query})
        if result.get("success") and result["data"]["content"]:
            return result["data"]["content"]
        else:
            return []

    def is_op(self, um):
        """
        获取直接下属列表
        :param um:
        :return:
        """
        return False

    def is_leader(self, um):
        result = self.get_resource("entity/search", {"schema": ["department", "team"], "q": "attributes.leader:*\(%s\)*" % um})
        return int(result["data"]["total"]) > 0