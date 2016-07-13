# Created by Leon Agmon Nacht


class FireWall(object):
    """
    a class representing a firewall (the ability to detect malicious packets)
    """
    def __init__(self, param_vector):
        """
        creates a firewall from the given data in param_vector
        :param param_vector: an instance of ParamVector that holds the needed data to define a FireWall instance
        :return: the new created FireWall instance
        """
        # the function that should return if a packet is malicious or not:
        self.func = FireWall.individual_firewall_generator(param_vector)

    @staticmethod
    def individual_firewall_generator(param_vector):
        """
        the method can create firewalls uniquely using the given param_vector
        :param param_vector: an instance of ParamVector that holds the needed data to define a FireWall instance
        :return: a new firewall defined entirely by the given data (param_vector)
        """
        # TODO: zemmel asked to implement

