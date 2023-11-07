import json

class Store:

  def __init__(self):
    self.data = {}

  def set(self, key, value):
    self.data[key] = value

  def get(self, key):
    keys = key.split('.')
    result = self.data
    for k in keys:
      result = result.get(k)
    return result

  def update(self, key, value):
    keys = key.split('.')
    temp = self.data
    for k in keys[:-1]:
      temp = temp.get(k)
    temp[keys[-1]] = value

  def delete(self, key):
    keys = key.split('.')
    temp = self.data
    for k in keys[:-1]:
      temp = temp.get(k)
    del temp[keys[-1]]

store = Store()
store.set('user.name', 'John')
print(store.get('user.name'))

store.update('user.name', 'Jane')
print(store.get('user.name'))

store.delete('user.name')
print(store.get('user'))