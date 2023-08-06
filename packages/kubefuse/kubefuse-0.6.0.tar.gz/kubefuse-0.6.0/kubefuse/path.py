import json
from datetime import datetime

class KubePath(object):
    def __init__(self, namespace = None, resource_type = None, object_id = None, action = None):
        self.namespace = namespace 
        self.resource_type = resource_type
        self.object_id = object_id
        self.action = None
        self.SUPPORTED_RESOURCE_TYPES = [
            'configmaps',
            'componentstatuses', 
            'daemonsets',
            'deployments',
            'endpoints',
            'events', 
            'horizontalpodautoscalers',
            'ingress',
            'jobs',
            'limits', 
            'nodes', 
            'pod', 
            'pv', 
            'pvc',
            'quota', 
            'rc', 
            'replicasets',
            'secrets',
            'serviceaccounts', 
            'svc', 
        ]
        self.SUPPORTED_ACTIONS = ['describe', 'json', 'yaml']
        self.SUPPORTED_POD_ACTIONS = ['logs'] + self.SUPPORTED_ACTIONS

    def parse_path(self, path):
        if path == '/': return self
        parts = path[1:].split("/")
        self.namespace = parts[0] if len(parts) > 0 else None
        self.resource_type = parts[1] if len(parts) > 1 else None
        self.object_id = parts[2] if len(parts) > 2 else None
        self.action = parts[3] if len(parts) > 3 else None
        return self

    def get_creation_date_for_action_file(self, client):
        if self.action not in ['json', 'yaml', 'describe']:
            return None
        metadata = client.get_object_in_format(
            self.namespace, self.resource_type,
            self.object_id, 'json')
        json_data = json.loads(metadata)
        ts = None
        if 'metadata' in json_data:
            if 'creationTimestamp' in json_data['metadata']:
                timestamp = json_data['metadata']['creationTimestamp']
                if timestamp is not None:
                    ts = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
                    ts = int(ts.strftime("%s"))
        return ts

    def is_dir(self):
        return self.action is None

    def is_file(self):
        return not(self.is_dir())

    def exists(self, client):
        if self.namespace is None:
            return True
        namespaces = client.get_namespaces()
        if self.namespace not in namespaces:
            return False
        if self.resource_type is None:
            return True
        if self.resource_type not in self.SUPPORTED_RESOURCE_TYPES:
            return False
        if self.object_id is None:
            return True
        entities = client.get_entities(self.namespace, self.resource_type)
        if self.object_id not in entities:
            return False
        if self.action is None:
            return True
        if self.resource_type == 'pod' and self.action in self.SUPPORTED_POD_ACTIONS:
            return True
        if self.action not in self.SUPPORTED_ACTIONS:
            return False
        return True

    def do_action(self, client):
        ns, rt, oid = self.namespace, self.resource_type, self.object_id
        if self.action == 'describe':
            return client.describe(ns, rt, oid)
        if self.action == 'logs':
            return client.logs(ns, oid)
        if self.action in ['json', 'yaml']:
            return client.get_object_in_format(ns, rt, oid, self.action)

    def get_mode(self):
        return 0o444 if self.action not in ['json', 'yaml'] else 0o666

    def __repr__(self):
        result = ['<']
        if self.action is not None:
            result.append("action %s on" % self.action)
        if self.object_id is not None:
            result.append('object %s' % self.object_id)
        if self.resource_type is not None:
            result.append("of type %s" % self.resource_type)
        if self.namespace is not None:
            result.append('in namespace %s' % self.namespace)
        result.append('>')
        return " ".join(result)
