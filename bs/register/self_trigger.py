#!/usr/bin/env python

import SitcpRbcp

rbcp = SitcpRbcp.SitcpRbcp()
#rbcp.set_verify_mode()
rbcp.set_timeout(1.0)

ip_address = {}
ip_address['x'] = '192.168.10.16'
ip_address['y'] = '192.168.10.17'

trigger_enable = {}
trigger_enable['address'] = 0x18
trigger_enable['x'] = 0b1111111111111111
trigger_enable['y'] = 0b1111111111111111

trigger_polarity = {}
trigger_polarity['address'] = 0x1A
trigger_polarity['x'] = 0b1111111111111111
trigger_polarity['y'] = 0b1111111111111111

trigger_delay = {}
trigger_delay['address'] = 0x1C
trigger_delay['x'] = 128
trigger_delay['y'] = 128

th = {}
th['x'] = {}
th['y'] = {}

# th['x' or 'y'][ch] = thres value

th['x'][0]  = 0
th['x'][1]  = 1
th['x'][2]  = 2
th['x'][3]  = 3
th['x'][4]  = 4
th['x'][5]  = 5
th['x'][6]  = 6
th['x'][7]  = 7
th['x'][8]  = 8
th['x'][9]  = 9
th['x'][10] = 10
th['x'][11] = 11
th['x'][12] = 12
th['x'][13] = 13
th['x'][14] = 14
th['x'][15] = 15

th['y'][0]  = 0
th['y'][1]  = 10
th['y'][2]  = 20
th['y'][3]  = 30
th['y'][4]  = 40
th['y'][5]  = 50
th['y'][6]  = 60
th['y'][7]  = 70
th['y'][8]  = 80
th['y'][9]  = 90
th['y'][10] = 100
th['y'][11] = 110
th['y'][12] = 120
th['y'][13] = 130
th['y'][14] = 140
th['y'][15] = 150

for a in ('x', 'y'):
    print '--->', ip_address[a]
    print "trigger_enable: %s" % (a),
    print "trigger_enable address: 0x%x 0x%x" % (trigger_enable['address'], trigger_enable[a])
    #rbcp.write_register_f(ip_address[a], trigger_enable['address'], '>H', trigger_enable[a])

    print "trigger_polality: %s" % (a),
    print "trigger_polarity address: 0x%x 0x%x" % (trigger_polarity['address'], trigger_polarity[a])
    #rbcp.write_register_f(ip_address[a], trigger_polarity['address'], '>H', trigger_polarity[a])

    print "trigger_delay: %s" % (a),
    print "trigger_delay address: 0x%x 0x%x" % (trigger_delay['address'], trigger_delay[a])
    #rbcp.write_register_f(ip_address[a], trigger_polarity['address'], '>H', trigger_polarity[a])

    for ch in sorted(th[a].keys()):
        adc_thres_base_address = 0x20
        print 'thr address: %02x' % (adc_thres_base_address + 2*ch),
        print 'ch: %d value: %d' % (ch, th[a][ch])
        #rbcp.write_register_f(ip_address[a], th[a][ch], '>H', th[a][ch])
