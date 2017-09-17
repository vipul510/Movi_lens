# importing pandas, numpy and matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading file 
ratings_movie_data = pd.read_csv("ratings.csv")

# generating numpy array
ratings_data = np.array(ratings_movie_data, dtype=float)
user_id = np.array(ratings_data[:,0], dtype = float)
movie_id= np.array(ratings_data[:,1], dtype = float)
ratings = np.array(ratings_data[:,2], dtype = float)

#filtering and arranging relevant DATA for movie vs rating plot
h= len(ratings)
m_id= list(set(movie_id))
u= list(set(user_id)) 
rate=[0]*len(m_id)
num = [0]*len(m_id)
idd = [0]* len(m_id)

#calculating average number of ratings and average ratings of each movie
for i in range (0, len(m_id)):
 j = movie_id == m_id[i]
 rate[i] = np.sum(ratings[j],dtype=float)
 num[i] = np.sum(j,dtype=float)
 idd[i] = m_id[i]
avg= np.divide(rate,num)

# finding user ID with maximum and minimum submissions of ratings and average rating by them
h= len(ratings)
u_id= np.unique(user_id)
jj=[0]*len(u_id)
nos =[0]*len(u_id)
avg_rating=[0]*len(u_id)
for i in range (0,len(u_id)):
 pp=user_id == u_id[i]
 var1=np.sum(ratings[pp])
 var2= np.sum(pp)
 nos[i] =var2
 avg_rating[i] = var1/var2
 jj[i] = var2

#user submitting maximum number of rating
rt= max(nos)
ind=nos.index(rt)
user_1 = u_id[ind]
print("User submitting maximum number of rating is ")
print(user_1)
print("total ratings submitted were")
print(rt)
avg_r= avg_rating[ind]
print("and average rating given by this user is")
print(avg_r)
print("************************")

#user submitting minimum number of rating
rt2= min(nos)
ind2=nos.index(rt2)
user_2 = u_id[ind2]
print("User submitting minimum number of rating is ")
print(user_2)
print("total ratings submitted were")
print(rt2)
avg_r2= avg_rating[ind2]
print("and average rating given by this user is")
print(avg_r2)
print("************************")

# finding movie with highest average rating
rt3= max(avg_rating)
ind3=avg_rating.index(rt3)
mov = m_id[ind3]
print("movie with highest average rating is movie with ID")
print(mov)
print("************************")

# plotting number of ratings vs average rating given to a particular movie
plt.scatter(avg, num, s= avg*50, alpha = 0.4, c=idd)
plt.xlabel('Average Rating of movies')
plt.ylabel('Number of times rating given to each movie')
plt.text(1, 70, 'color variation as per movie ID')
plt.xlim(0.5, 5.5)
plt.grid(True)
plt.colorbar()
plt.show()

#plotting average rating given by user vs user ID
plt.scatter(u_id,avg_rating,  s= jj*50, alpha = 0.4, c=jj)
plt.xlabel('user id')
plt.ylabel('average rating given by user')
plt.text(40, 4.35, 'User ID-53')
plt.text(0,4.8 , 'color variation as per number of ratings given')
plt.xlim(-10, 130)
plt.grid(True)
plt.colorbar()
plt.show()
