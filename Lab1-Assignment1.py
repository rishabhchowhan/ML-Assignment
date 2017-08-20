
# coding: utf-8

# In[1]:

#(a−b)2=a2+b2−2ab
import tensorflow as tf
a = tf.constant(2)
b = tf.constant(3)
pr1 = tf.multiply(a,a, name="Square_variable_a")
pr2 = tf.multiply(b,b, name="Square_variable_b")
pr3 = tf.multiply(a,b, name="Multiply_a_and_b")
pr4 = tf.multiply(2,pr3, name="Result_of_2ab")
res1 = tf.add(pr1,pr2)
res2 = tf.subtract(res1,pr4, name="Final_Result")

with tf.Session() as sess:
    writer = tf.summary.FileWriter("/tmp/tboard/output_Assignment", sess.graph)
    print(sess.run(res2))
    writer.close()


# In[ ]:




# In[ ]:



