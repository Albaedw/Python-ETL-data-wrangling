#!/usr/bin/env python
cars = {'Car': { 'type': { 'suv'        : {'color': ['red','yellow','black']
                                          },
                           'truck' : {'big': { 'color' : ['red','yellow'],
                                               'weight': ['heavy']
                                                    },
                                      'small': {'color' : ['black','red'],
                                                'weight': ['light'],
                                                'length': ['short','long']
                                               }
                                      }
                          }
                      },
               'exterior' : {'color' : ['green','red']}
             }
#Let's say we need to find only "red" attribute on a leaf/list level of many nested dictionaries

def filterNestedDict(node, searchItem):
    if isinstance(node,list):
       for x in node:
          if x == searchItem:
           return node
       return None
    else:
        f_node={}
        for key, val in node.iteritems():
            cur_node = filterNestedDict(val, searchItem)
            if cur_node:
              f_node[key] = cur_node
        return f_node or None

res=filterNestedDict(cars, "red")
print res
