import yaml

# class ObjectData(yaml.YAMLObject):
#     yaml_loader = yaml.SafeLoader
#     yaml_tag = u'!ObjectData'

#     def __init__(self, obj_type , type_id , instance_id , description, dist_x = 0, dist_y = 0, height = 0, width = 0, angle = 0, rotation_direction = 0):
#         self.distance_to_center_x = dist_x
#         self.distance_to_center_y = dist_y
#         self.height = height
#         self.width = width
#         self.angle = angle
#         self.rotation_direction = rotation_direction
#         self.description = description
#         self.type = obj_type
#         self.type_id = type_id
#         self.instance_id = instance_id
class ObjectData(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!ObjectData'

    def __init__(self, obj_type , type_id , instance_id , description, pos_x = 0, pos_y = 0, rotation_angle = 0):
        self.description = description
        self.type = obj_type
        self.type_id = type_id
        self.instance_id = instance_id
        self.position_x = pos_x
        self.position_y = pos_y  
        self.rotation_angle = rotation_angle
        self.is_picked   = False
        self.is_placed   = False
        self.is_found    = False
        
