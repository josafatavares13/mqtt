# mqtt_python_postgreSQL
# main em desenvonvimento 
################################################# FRONIUS 1° DATABASE ########################################################

  - name: "Potência Total AC"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/Power"
    unit_of_measurement: "W"
    value_template: "{{value_json['value']}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Energia Total AC"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/Energy/Forward"
    unit_of_measurement: "Wh"
    value_template: "{{value_json['value']}}"
    payload_available: "online"
    payload_not_available: "offline"
    
# Fase 1 Fronius
  - name: "Potência AC L1"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L1/Power"
    unit_of_measurement: "W"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Energia AC L1"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L1/Energy/Forward"
    unit_of_measurement: "Wh"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"

  - name: "Tensão AC L1"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L1/Voltage"
    unit_of_measurement: "V"
    value_template: "{{value_json['value']}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Corrente AC L1"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L1/Current"
    unit_of_measurement: "A"
    value_template: "{{value_json['value']}}"
    payload_available: "online"
    payload_not_available: "offline"
    
# Fase 2 Fronius
  - name: "Potência AC L2"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L2/Power"
    unit_of_measurement: "W"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Energia AC L2"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L2/Energy/Forward"
    unit_of_measurement: "Wh"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"

  - name: "Tensão AC L2"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L2/Voltage"
    unit_of_measurement: "V"
    value_template: "{{value_json['value']}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Corrente AC L2"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L2/Current"
    unit_of_measurement: "A"
    value_template: "{{value_json['value']}}"
    payload_available: "online"
    payload_not_available: "offline"
    
# Fase 3 Fronius
  - name: "Potência AC L3"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L3/Power"
    unit_of_measurement: "W"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Energia AC L3"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L3/Energy/Forward"
    unit_of_measurement: "Wh"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"

  - name: "Tensão AC L3"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L3/Voltage"
    unit_of_measurement: "V"
    value_template: "{{value_json['value']}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Corrente AC L3"
    state_topic: "N/102c6b9d30f3/pvinverter/20/Ac/L3/Current"
    unit_of_measurement: "A"
    value_template: "{{value_json['value']}}"
    payload_available: "online"
    payload_not_available: "offline"

# Potências Injetadas na Rede
  - name: "Potência Injetada na Rede - L1"
    state_topic: "N/102c6b9d30f3/system/0/Ac/Grid/L1/Power"
    unit_of_measurement: "W"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Potência Injetada na Rede - L2"
    state_topic: "N/102c6b9d30f3/system/0/Ac/Grid/L2/Power"
    unit_of_measurement: "W"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Potência Injetada na Rede - L3"
    state_topic: "N/102c6b9d30f3/system/0/Ac/Grid/L3/Power"
    unit_of_measurement: "W"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
################################################# BATERIA BYD 2° DATABASE ####################################################

  - name: "Potência da Bateria"
    state_topic: "N/102c6b9d30f3/system/0/Dc/Battery/Power"
    unit_of_measurement: "W"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Tensão da Bateria"
    state_topic: "N/102c6b9d30f3/system/0/Dc/Battery/Voltage"
    unit_of_measurement: "V"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Corrente da Bateria"
    state_topic: "N/102c6b9d30f3/system/0/Dc/Battery/Current"
    unit_of_measurement: "A"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"    
    
  - name: "SoC"
    state_topic: "N/102c6b9d30f3/system/0/Dc/Battery/Soc"
    unit_of_measurement: "%"
    value_template: "{{value_json['value']|round(2,'common')}}"
    payload_available: "online"
    payload_not_available: "offline"
    
################################################# ALARMES #################################################################

# Alarmes da Bateria

  - name: "Temperatura Alta na Carga - BYD"
    state_topic: "N/102c6b9d30f3/battery/512/Alarms/HighChargeTemperature"
    payload_available: "online"
    payload_not_available: "offline"
    
  - name: "Temperatura Baixa na Carga - BYD"
    state_topic: "N/102c6b9d30f3/battery/512/Alarms/LowChargeTemperature"
    payload_available: "online"
    payload_not_available: "offline"