from flask import Blueprint, jsonify, request
import sys, struct, socket

wol = Blueprint(name="wol", import_name=__name__)

broadcast = ['192.168.1.255', '192.168.0.255']
port = 9

@wol.route('', methods=['POST'])
def wake_on_lan():
    """
    ---
    post:
      description: Turns on a computer remotely
      requestBody:
        required: true
        content:
            application/json:
                schema: InputSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
        '400':
          description: call fail
          content:
            application/json:
              schema: ErrorSchema
      tags:
          - wake on lan
    """
    try:
        data = request.get_json()
        mac_address = data['mac_address']
        add_oct = mac_address.split(':')
        hwa = struct.pack('BBBBBB', int(add_oct[0],16),
                                    int(add_oct[1],16),
                                    int(add_oct[2],16),
                                    int(add_oct[3],16),
                                    int(add_oct[4],16),
                                    int(add_oct[5],16))

        msg = '\xff'.encode() * 6 + hwa * 16

        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
        
        for i in broadcast:
            soc.sendto(msg,(i,port))
        soc.close()

        output  = {"message": "Turning on the computer"}
        return jsonify(output), 200
    except:
        output  = {"message": "Something went wrong"}
        return jsonify(output), 400