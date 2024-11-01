#!/usr/bin/env python3
"""
Unittests for utils
"""

from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized  # Import directly


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to Test GithubOrg
    """
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, cmp, expected, mock_getJson):
        """
        Test Org Method
        """
        mock_getJson.return_value = expected
        org_class = GithubOrgClient(cmp)
        result = org_class.org
        mock_getJson.assert_called_once_with(org_class.ORG_URL.format(org=cmp))
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """
        Class to Test _public_repos_url
        """
        payload = {
            'payload': 'hello'
        }
        with patch.object(
            GithubOrgClient, 
            'org', 
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient('clientORG')
            org_data = client.org
            self.assertEqual(org_data, payload)
