import riak

# myClient = riak.RiakClient(pb_port=8087, protocol='pbc')

# Because the Python client uses the Protocol Buffers interface by
# default, the following will work the same:
myClient = riak.RiakClient(pb_port=8087)

# First, let's create a few objects and a bucket to keep them in.

myBucket = myClient.bucket('test')

val1 = 1
key1 = myBucket.new('one', data=val1)
key1.store()
#we have stored the integer 1 with the lookup key of one
val2 = "two"
key2 = myBucket.new('two', data=val2)
key2.store()

# Finally, let's store a bit of JSON.
val3 = {"myValue": 3}
key3 = myBucket.new('three', data=val3)
key3.store()

# Now that we have a few objects stored, let's retrieve them and make sure they contain the values we expect.

fetched1 = myBucket.get('one')
fetched2 = myBucket.get('two')
fetched3 = myBucket.get('three')

print (fetched1.data)
print(fetched2.data)
print (fetched3.data)
assert val1 == fetched1.data
assert val2 == fetched2.data
assert val3 == fetched3.data

#Updating Objects In Riak
fetched3.data["myValue"] = 42
fetched3.store()

# Deleting Objects From Riak
fetched1.delete()
fetched2.delete()
fetched3.delete()

assert myBucket.get('one').exists == False
assert myBucket.get('two').exists == False
assert myBucket.get('three').exists == False

# Working With Complex Objects
book = {
  'isbn': "1111979723",
  'title': "Moby Dick",
  'author': "Herman Melville",
  'body': "Call me Ishmael. Some years ago...",
  'copies_owned': 3
}

booksBucket = myClient.bucket('books')
newBook = booksBucket.new(book['isbn'], data=book)
newBook.store()

fetchedBook = booksBucket.get(book['isbn'])

# Json
print(fetchedBook.encoded_data)

# Deserialized
# fetchedBook.data
fetchedBook.delete()
