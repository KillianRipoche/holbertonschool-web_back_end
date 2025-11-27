#!/usr/bin/env python3
""" File for test client.py
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """ Class TestGithubOrgClient
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch("client.get_json")
    def test_org(self, org, test_payload, mock_get_json):
        """ Test org method
        """
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org)

        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with
        (f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """ Test _public_repos_url
        """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """ Test public_repos
        """
        payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = payload
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock:
            mock.return_value = "https://api.github.com/orgs/google/repos"

            client = GithubOrgClient("google")
            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2"])

            mock.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test has_license
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


org_payload = {
    "login": "google",
    "id": 1342004,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
    "url": "https://api.github.com/orgs/google",
    "repos_url": "https://api.github.com/orgs/google/repos",
}

repos_payload = [
    {
        "id": 1,
        "name": "repo1",
        "full_name": "google/repo1",
        "license": {"key": "apache-2.0"}
    },
    {
        "id": 2,
        "name": "repo2",
        "full_name": "google/repo2",
        "license": {"key": "mit"}
    }
]

expected_repos = ["repo1", "repo2"]
apache2_repos = ["repo1"]


@parameterized_class([
    {"org_payload": org_payload,
     "repos_payload": repos_payload,
     "expected_repos": expected_repos,
     "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient methods
    """

    @classmethod
    def setUpClass(cls):
        """Set up class method to patch requests.get"""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Configure the mock to return the appropriate fixture
        mock_get.side_effect = cls.get_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patcher"""
        cls.get_patcher.stop()

    @staticmethod
    def get_side_effect(url):
        """Side effect method to return the appropriate fixture based on the
        URL"""
        if url == "https://api.github.com/orgs/google":
            return Mock(json=lambda: org_payload)
        if url == "https://api.github.com/orgs/google/repos":
            return Mock(json=lambda: repos_payload)
        return Mock(json=lambda: {})

    def test_public_repos(self):
        """Test the public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
