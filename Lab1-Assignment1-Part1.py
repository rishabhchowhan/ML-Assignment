
# coding: utf-8

# In[4]:

# (a−b)3=a3−b3+3ab(a−b)
import tensorflow as tf
a = tf.constant(5)
b = tf.constant(4)
# multiplication of a 
p1 = tf.multiply(a,a)
p2 = tf.multiply(p1,a, name="Cube_of_a")
# multiplication of b
p3 = tf.multiply(b,b)
p4 = tf.multiply(p3,b, name="Cube_of_a")
# 3*a*b
p5 = tf.multiply(3,a)
p6 = tf.multiply(p5,b, name="3_a_b")
# a-b
p7 = tf.subtract(a,b, name="a_-_b")
# 3ab(a−b)
p8 = tf.multiply(p7,p6)
# a3−b3
p9 = tf.subtract(p2,p4, name="a3_-_b3")
res = tf.add(p9,p8, name="Result")

with tf.Session() as sess:
    writer = tf.summary.FileWriter("/tmp/tboard/output", sess.graph)
    print(sess.run(res))
    writer.close()


# In[ ]:



