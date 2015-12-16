#! /usr/bin/env python3

#######################
# CloudGenerator_standalone.py
#
# this is intended for when autonomous ambient shifting 
# light is desired with no external input 
#
########################

import opc
import sys
import time
import math
import perlin
import json
import os


class CloudGenerator(object):

    def __init__(self, verbose = True):
        # definitions, settings

        self.dx = 0
        self.dy = 0
        self.VERBOSE = verbose
        settings = '' 
        path = os.path.dirname(os.path.abspath(__file__))

        with open(path + '/config.json') as config:
            settings = json.load(config)
        self.init_settings(settings)

        # initialize OPC connecion
        self.client = opc.Client('localhost:7890', True)
        self.client._ensure_connected()

    def init_settings(self, config):
        if config == '':
            config["speed"] = 0.01
            config["size"]["width"] = 4
            config["size"]["height"] = 64
            config["noise_tile_size"] = 512

        self.width = config["size"]["width"]
        self.height = config["size"]["height"]
        self.speed = config["speed"]
        self.simplex = perlin.SimplexNoise(config["noise_tile_size"])
        self.pixels = [(0,0,0)] * self.width * self.height	


    def fractalNoise(self, x, y, z):
        r = 0
        amp = 1.0
        for i in range(0, 4): 
            r += self.simplex.noise3(x,y,z)
            amp /= 2
            x *= 2
            y *= 2
            z *= 2

        return r

    def log(self, msg):
        if not self.VERBOSE:
            return
        print(msg)
    
    
# main loop
    def draw(self):
        now = time.clock()
        angle = math.sin(now * .001)
        z = now * .00008
        hue = now * .01
        scale = .005

        self.dx += math.cos(angle) * self.speed
        self.dy += math.sin(angle) * self.speed

        for x in range(self.width):
            for y in range(self.height):
                n = self.fractalNoise(self.dx + x * scale, self.dy + y * scale, z) - 0.75
                m = self.fractalNoise(self.dx + x * scale, self.dy + y * scale, z + 10) - 0.75


                color = (
                    (hue + 80 * abs(m)) % 255,
                    255 - 100 * max(min(math.pow(3.0 * abs(n), 3.5), 1.0), .6),
                    255 * max(min(math.pow(3.0 * abs(n), 1.5), .3), .6)
                    )

                self.pixels[x + self.width * y] = color

        self.client.put_pixels(self.pixels)



clouds = CloudGenerator()


# wait while socket is created
time.sleep(2)


while (True):
	clouds.draw()
	time.sleep(0.01)
