# -*- coding: utf-8 -*-
from enum import auto
from odoo import http
import logging
_logger = logging.getLogger(__name__)

# filter search class
class Filter:
    def filter_tree(self,kwargs):
        #filter based in odoo operator conditions
        if kwargs["filter_by"] == "0":
            kwargs["filter_by"] = "ilike"
            # send search attributes to the db

        elif kwargs["filter_by"] == "1":
            kwargs["filter_by"] = "="            

        elif kwargs["filter_by"] == "2":
            kwargs["filter_by"] = "start_by" 

        elif kwargs["filter_by"] == "3":
            kwargs["filter_by"] = "finish_by" 
        
        ## redefine container condition with the service  ##
        container = {
                "records": [
                    {
                        "name": "Jonh", 
                        "last_name": "Doe",
                        "nationality": "Canadian",
                        "phone_number": "+2",
                        "address":"address",
                        "id": "123",
                        "document_id":"111",
                        "email": "noone@sample.com",
                        "civil_status": "married",
                        "age": "23",
                        "img": "static/img/profile.png",
                    },
                    {
                        "name": "Jonhy", 
                        "last_name": "Doewy",
                        "nationality": "German",
                        "phone_number": "+25",
                        "address":"address",
                        "id": "222",
                        "document_id":"444",
                        "email": "me@sample.com",
                        "civil_status": "single",
                        "age": "21",
                        "img": "static/img/profile.png",
                    }
                ]
        }    
        ## redefine container condition with the service  ##

        return container

    def filter_kanban(self,kwargs):
        #filter based in odoo operator conditions
        if kwargs["filter_by"] == "0":
            kwargs["filter_by"] = "ilike"
            # send search attributes to the db

        elif kwargs["filter_by"] == "1":
            kwargs["filter_by"] = "="            

        elif kwargs["filter_by"] == "2":
            kwargs["filter_by"] = "start_by" 

        elif kwargs["filter_by"] == "3":
            kwargs["filter_by"] = "finish_by" 
        
        ## redefine container condition with the service  ##
        container = {
                "_metadata":{
                        "page": kwargs["page"],
                        "per_page": kwargs["pagination"],
                        "page_count": 20,
                        "total_count": 521,
                        "links": [
                            {"self": "/products?page=5&per_page=20"},
                            {"first": "/products?page=0&per_page=20"},
                            {"previous": "/products?page=4&per_page=20"},
                            {"next": "/products?page=6&per_page=20"},
                            {"last": "/products?page=26&per_page=20"},
                        ]
                    },
                "records": [
                    {
                        "name": "Jonh", 
                        "last_name": "Doe",
                        "nationality": "Canadian",
                        "phone_number": "+2",
                        "address":"address",
                        "id": "123",
                        "document_id":"111",
                        "email": "noone@sample.com",
                        "civil_status": "married",
                        "age": "23",
                        "img": "static/img/profile.png",
                    },
                    {
                        "name": "Jonhy", 
                        "last_name": "Doewy",
                        "nationality": "German",
                        "phone_number": "+25",
                        "address":"address",
                        "id": "222",
                        "document_id":"444",
                        "email": "me@sample.com",
                        "civil_status": "single",
                        "age": "21",
                        "img": "static/img/profile.png",
                    }
                ]
        }    
        ## redefine container condition with the service  ##

        return container

# inherit from my filter class to add some search conditions
class ClientSearch(http.Controller,Filter):
    @http.route("/client_search", type="json", auth="user", website=True)
    def index(self):
        return {"info":"info"}
    
    # renamed route /client_search_by to /client_search_tree 
    @http.route("/client_search_tree", type="json", auth="user", website=True)
    def search_tree(self,**kwargs):
        # translate pagination option to amount of items per page

        if kwargs["search_box"]!="":
            # search and filter conditions
            if kwargs["search_by"] == "0":
                kwargs["search_by"] = "name"
                container = super().filter_tree(kwargs)
                
            if kwargs["search_by"] == "1":
                kwargs["search_by"] = "last_name"
                container = super().filter_tree(kwargs)
            
            if kwargs["search_by"] == "2":
                kwargs["search_by"] = "full_name"
                container = super().filter_tree(kwargs)

            if kwargs["search_by"] == "3":
                kwargs["search_by"] = "email"
                container = super().filter_tree(kwargs)

            if kwargs["search_by"] == "4":
                kwargs["search_by"] = "reservation_id"
                container = super().filter_tree(kwargs)

            if kwargs["search_by"] == "5":
                kwargs["search_by"] = "phone_number"
                container = super().filter_tree(kwargs)

            ## data return to js as a dictionary with metadata and an array with the query ##
            return container

        else:
            return False  

    @http.route("/client_search_kanban" , type="json", auth="user", website=True)
    def search_kanban(self,**kwargs):
        # translate pagination option to amount of items per page
        if kwargs["pagination"] == "0":
            kwargs["pagination"] = 10

        elif kwargs["pagination"] == "1":
            kwargs["pagination"] = 25

        elif kwargs["pagination"] == "2":
            kwargs["pagination"] = 50

        elif kwargs["pagination"] == "3":
            kwargs["pagination"] = 100

        if kwargs["search_box"]!="":
            # search and filter conditions
            if kwargs["search_by"] == "0":
                kwargs["search_by"] = "name"
                container = super().filter_kanban(kwargs)
                
            if kwargs["search_by"] == "1":
                kwargs["search_by"] = "last_name"
                container = super().filter_kanban(kwargs)
            
            if kwargs["search_by"] == "2":
                kwargs["search_by"] = "full_name"
                container = super().filter_kanban(kwargs)

            if kwargs["search_by"] == "3":
                kwargs["search_by"] = "email"
                container = super().filter_kanban(kwargs)

            if kwargs["search_by"] == "4":
                kwargs["search_by"] = "reservation_id"
                container = super().filter_kanban(kwargs)

            if kwargs["search_by"] == "5":
                kwargs["search_by"] = "phone_number"
                container = super().filter_kanban(kwargs)

            ## data return to js as a dictionary with metadata and an array with the query ##
            return container

        else:
            return False

    @http.route("/get_client_profile_url", type="json", auth="user", website=True)
    def make_url_client_profile(self,**kwargs):
        ir_action = http.request.env["ir.actions.actions"]
        action = ir_action.search([("name","=","Perfil del Cliente")])

        url = f"""http://localhost:9000/web#action={action.id}&user_id={kwargs['id']}"""
        return {"url":url}