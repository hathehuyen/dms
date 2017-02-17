from flask import Blueprint, request, jsonify
from app.common.models import DC, Rack, Server, HDD
import json
from bson import ObjectId


mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/', methods=['GET', 'POST'])
def index():
    return "API"


@mod_api.route('/dc', methods=['GET', 'POST'])
def dc_api():
    try:
        # Get data center list
        if request.method == 'GET':
            if '_id' in request.values:
                dcs = DC.objects(id=ObjectId(json.loads(request.values['_id'])['$oid']))
            else:
                dcs = DC.objects
            return jsonify(result=True, dcs=dcs)
        # Create new data center
        if request.method == 'POST':
            dc = DC()
            dc.name = request.values['name']
            dc.save()
            return jsonify(result=True, dc=dc)
        return jsonify(result=False)
    except Exception as exc:
        print(exc)
        print 'data center error'
        print request.values
        return jsonify(result=False)


@mod_api.route('/rack', methods=['GET', 'POST'])
def rack_api():
    try:
        # Get rack list
        if request.method == 'GET':
            if '_id' in request.values:
                racks = Rack.objects(id=ObjectId(json.loads(request.values['_id'])['$oid']))
            elif 'dc_id' in request.values:
                dc = DC.objects(id=ObjectId(json.loads(request.values['dc_id'])['$oid']))[0]
                racks = Rack.objects(dc=dc)
            else:
                racks = Rack.objects
            return jsonify(result=True, racks=racks)
        # Create new rack
        if request.method == 'POST':
            rack = Rack()
            rack.name = request.values['name']
            dc = DC.objects(id=ObjectId(json.loads(request.values['dc_id'])['$oid']))[0]
            rack.dc = dc
            rack.save()
            return jsonify(result=True, rack=rack)
        return jsonify(result=False)
    except Exception as exc:
        print(exc)
        print 'rack error'
        print request.values
        return jsonify(result=False)


@mod_api.route('/server', methods=['GET', 'POST'])
def server_api():
    try:
        # Get server list
        if request.method == 'GET':
            if '_id' in request.values:
                servers = Server.objects(id=ObjectId(json.loads(request.values['_id'])['$oid']))
            elif 'mac' in request.values:
                servers = Server.objects(mac=request.values['mac'])
            elif 'rack_id' in request.values:
                rack = Rack.objects(id=ObjectId(json.loads(request.values['rack_id'])['$oid']))[0]
                servers = Server.objects(rack=rack)
            else:
                servers = Server.objects
            return jsonify(result=True, servers=servers)
        # Create new server
        if request.method == 'POST':
            if 'mac' in request.values:
                server = Server()
                server.ip = request.values['ip']
                server.mac = request.values['mac']
                rack = Rack.objects(id=ObjectId(json.loads(request.values['rack_id'])['$oid']))[0]
                server.rack = rack
                server.save()
                return jsonify(result=True, server=server)
            else:
                return jsonify(result=False)
        return jsonify(result=False)
    except Exception as exc:
        print(exc)
        print 'get server error'
        print request.values
        return jsonify(result=False)


@mod_api.route('/hdd', methods=['GET', 'POST', 'PUT'])
def hdd_api():
    try:
        # Get HDD list
        if request.method == 'GET':
            if '_id' in request.values:
                hdds = HDD.objects(id=ObjectId(json.loads(request.values['_id'])['$oid']))
            elif 'serial' in request.values:
                hdds = HDD.objects(serial=request.values['serial'])
            elif 'server_id' in request.values:
                server = Rack.objects(id=ObjectId(json.loads(request.values['server_id'])['$oid']))[0]
                hdds = HDD.objects(server=server)
            else:
                hdds = HDD.objects
            return jsonify(result=True, hdds=hdds)
        # Create new HDD
        if request.method == 'POST':
            if 'serial' in request.values:
                hdd = HDD()
                hdd.serial = request.values['serial']
                if 'capacity' in request.values:
                    hdd.capacity = request.values['capacity']
                if 'used' in request.values:
                    hdd.used = request.values['used']
                if 'status' in request.values:
                    hdd.status = request.values['status']
                if 'server_id' in request.values:
                    server = Server.objects(id=ObjectId(json.loads(request.values['server_id'])['$oid']))[0]
                    hdd.server = server
                hdd.save()
                return jsonify(result=True, hdd=hdd)
            else:
                return jsonify(result=False)
        # Update HDD status
        if request.method == 'PUT':
            if 'serial' in request.values:
                hdd = HDD.objects(serial=request.values['serial'])[0]
                if 'capacity' in request.values:
                    hdd.capacity = request.values['capacity']
                if 'used' in request.values:
                    hdd.used = request.values['used']
                if 'status' in request.values:
                    hdd.status = request.values['status']
                hdd.save()
                return jsonify(result=True, hdd=hdd)
        return jsonify(result=False)
    except Exception as exc:
        print(exc)
        print 'get hdd error'
        print request.values
        return jsonify(result=False)
