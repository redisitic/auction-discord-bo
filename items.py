import json
import time
import uuid

class Items():
    def __init__(self, id:str = None, parameters:dict = None):
        if id is None:
            self.id = str(uuid.uuid4())
            if parameters is None:
                raise ValueError("Parameters must be provided if id is not provided")
            self.name = parameters.get("name", None)
            self.starting_bid = parameters.get("starting_bid", None)
            self.auction_time = parameters.get("auction_time", None)
            self.autobuy = parameters.get("autobuy", None)
            current_time = int(time.time())
            to_dump = {
                "id": self.id,
                "name": self.name,
                "starting_bid": self.starting_bid,
                "start_time": current_time,
                "end_time": current_time + self.auction_time,
                "autobuy": self.autobuy,
                "current_bid": self.starting_bid
            }
            current_items = json.load(open("items.json", "r"))
            current_items[self.id] = to_dump
            json.dump(current_items, open("items.json", "w"))
        else:
            current_items = json.load(open("items.json", "r"))
            if id not in current_items:
                raise ValueError("Item not found")
            self.id = id
            self.name = current_items[id]["name"]
            self.starting_bid = current_items[id]["starting_bid"]
            self.start_time = current_items[id]["start_time"]
            self.end_time = current_items[id]["end_time"]
            self.autobuy = current_items[id]["autobuy"]
            self.current_bid = current_items[id]["current_bid"]
            
            
    def  __str__(self) -> str:
        return f"Item: {self.name} \n Starting Bid: {self.starting_bid} \n Current Bid: {self.current_bid} | Autobuy: {self.autobuy}"