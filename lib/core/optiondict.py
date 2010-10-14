#!/usr/bin/env python

"""
$Id$

Copyright (c) 2006-2010 sqlmap developers (http://sqlmap.sourceforge.net/)
See the file doc/COPYING for copying permission.
"""

optDict = {
            # Format:
            # Family:        { "parameter name":    "parameter datatype" },
            # Or:
            # Family:        { "parameter name":    ("parameter datatype", "category name used for common outputs feature") },
            "Target":        {
                               "direct":            "string",
                               "url":               "string",
                               "list":              "string",
                               "requestFile":       "string",
                               "googleDork":        "string",
                               "configFile":        "string"
                             },

            "Request":       {
                               "method":            "string",
                               "data":              "string",
                               "cookie":            "string",
                               "cookieUrlencode":   "boolean",
                               "dropSetCookie":     "boolean",
                               "referer":           "string",
                               "agent":             "string",
                               "userAgentsFile":    "string",
                               "headers":           "string",
                               "aType":             "string",
                               "aCred":             "string",
                               "aCert":             "string",
                               "keepAlive":         "boolean",
                               "proxy":             "string",
                               "pCred":             "string",
                               "ignoreProxy":       "boolean",
                               "threads":           "integer",
                               "delay":             "float",
                               "timeout":           "float",
                               "retries":           "integer",
                               "scope":             "string",
                               "safUrl":            "string",
                               "saFreq":            "integer"
                             },

            "Injection":     {
                               "testParameter":     "string",
                               "dbms":              "string",
                               "os":                "string",
                               "prefix":            "string",
                               "postfix":           "string",
                               "string":            "string",
                               "regexp":            "string",
                               "eString":           "string",
                               "eRegexp":           "string",
                               "thold":             "float",
                               "useBetween":        "boolean",
                               "space":             "string",
                             },

            "Techniques":    {
                               "stackedTest":       "boolean",
                               "timeTest":          "boolean",
                               "timeSec":           "integer",
                               "unionTest":         "boolean",
                               "uTech":             "string",
                               "unionUse":          "boolean"
                             },

            "Fingerprint":   {
                               "extensiveFp":       "boolean"
                             },

            "Enumeration":   {
                               "getBanner":         ("boolean", "Banners"),
                               "getCurrentUser":    ("boolean", "Users"),
                               "getCurrentDb":      ("boolean", "Databases"),
                               "isDba":             "boolean",
                               "getUsers":          ("boolean", "Users"),
                               "getPasswordHashes": ("boolean", "Passwords"),
                               "getPrivileges":     ("boolean", "Privileges"),
                               "getRoles":          ("boolean", "Roles"),
                               "getDbs":            ("boolean", "Databases"),
                               "getTables":         ("boolean", "Tables"),
                               "getColumns":        ("boolean", "Columns"),
                               "dumpTable":         "boolean",
                               "dumpAll":           "boolean",
                               "search":            "boolean",
                               "user":              "string",
                               "db":                "string",
                               "tbl":               "string",
                               "col":               "string",
                               "excludeSysDbs":     "boolean",
                               "limitStart":        "integer",
                               "limitStop":         "integer",
                               "firstChar":         "integer",
                               "lastChar":          "integer",
                               "query":             "string",
                               "sqlShell":          "boolean"
                             },

            "User-defined function": {
                               "udfInject":         "boolean",
                               "shLib":             "string"
                             },

            "File system":   {
                               "rFile":             "string",
                               "wFile":             "string",
                               "dFile":             "string"
                             },

            "Takeover":      {
                               "osCmd":             "string",
                               "osShell":           "boolean",
                               "osPwn":             "boolean",
                               "osSmb":             "boolean",
                               "osBof":             "boolean",
                               "privEsc":           "boolean",
                               "msfPath":           "string",
                               "tmpPath":           "string"
                             },

            "Windows":       {
                               "regRead":           "boolean",
                               "regAdd":            "boolean",
                               "regDel":            "boolean",
                               "regKey":            "string",
                               "regVal":            "string",
                               "regData":           "string",
                               "regType":           "string"
                             },

            "Miscellaneous": {
                               "xmlFile":           "string",
                               "sessionFile":       "string",
                               "flushSession":      "boolean",
                               "eta":               "boolean",
                               "googlePage":        "integer",
                               "updateAll":         "boolean",
                               "batch":             "boolean",
                               "cleanup":           "boolean",
                               "replicate":         "boolean",
                               "verbose":           "integer"
                             },
          }
