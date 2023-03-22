import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
from QueryMetadataParser import ConnectToGithub

class SQLQueryToLinkedList():

    def __init__(self, sql_query):
        self.sql_query = sql_query

    def stringToListNode(stringTotal):
        previousNode = None
        first = None
        for i in stringTotal:
            currentNode = ListNode(i)
            if first is None:
                first = currentNode
            if previousNode is not None:
                previousNode.next = currentNode
            previousNode = currentNode
        return first

if __name__ == "__main__":


