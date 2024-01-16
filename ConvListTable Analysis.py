#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[7]:


df = pd.read_csv('/Users/vaibhav.srivastava/Downloads/ConvListTable - ConvListTable.csv')


# In[8]:


df


# In[12]:


df['eval comment'].value_counts()


# In[13]:


# Data only for unique msgs

unique_msg_df = df[df['eval comment'].isin(['Y', 'N'])]


# In[15]:


unique_msg_df


# In[18]:


# Count and Percentage of unique msgs


value_counts = unique_msg_df['eval comment'].value_counts()
total_count = unique_msg_df['eval comment'].count()

percentage_counts = (value_counts / total_count) * 100

print("Value Counts:")
print(value_counts)

print("\nPercentage Counts:")
print(percentage_counts)

print("\nTotal Count:")
print(total_count)


# In[106]:


# BAR GRAPH


import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you already have unique_msg_df
# If not, replace 'your_file.csv' with the actual file path
# unique_msg_df = pd.read_csv('your_file.csv')

# Count plot
plt.figure(figsize=(8, 6))
ax = sns.countplot(data=unique_msg_df, x='eval comment')

# Annotate each bar with its percentage
total = len(unique_msg_df)
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height() / total)
    x = p.get_x() + p.get_width() / 2
    y = p.get_height() + 0.01
    ax.annotate(percentage, (x, y), ha='center')

plt.title("Count of Unique Messages")
plt.xlabel("eval Comment")
plt.ylabel("Count")
plt.show()


# In[105]:


#count of error types(N)

unique_msg_df['error type'].value_counts()


# In[104]:


# Total no. of unique conv.

unique_conv_id_count = unique_msg_df['conv_id'].nunique()
print("Total Unique Count of 'conv_id':", unique_conv_id_count)


# In[ ]:


# DataFrame for unique conv with 1 msg



# In[46]:


import pandas as pd

# Assuming you already have unique_msg_df
# If not, replace 'your_file.csv' with the actual file path
# unique_msg_df = pd.read_csv('your_file.csv')

# Filter the DataFrame to include only 'Y' and 'N' values
filtered_df = unique_msg_df[unique_msg_df['eval comment'].isin(['Y', 'N'])]

# Count occurrences of each 'conv_id'
conv_id_counts = filtered_df['conv_id'].value_counts()

# Filter 'conv_id' with count equal to 2
selected_conv_ids = conv_id_counts[conv_id_counts == 1].index

# Filter the DataFrame based on selected 'conv_id'
count1_result_df = filtered_df[filtered_df['conv_id'].isin(selected_conv_ids)]

# Now, result_df contains rows where 'eval comment' is 'Y' or 'N' and 'conv_id' count is 1


# In[47]:


count1_result_df


# In[50]:


# Total count of coversation with 1 msg

new_unique_conv_id_count = count1_result_df['conv_id'].nunique()
new_unique_conv_id_count


# In[49]:


# Count & Precentage -  of success and failure for conv with 1 msg



import pandas as pd

# Assuming you already have unique_msg_df
# If not, replace 'your_file.csv' with the actual file path
# unique_msg_df = pd.read_csv('your_file.csv')

# Filter the DataFrame to include only 'Y' and 'N' values
filtered_df = count1_result_df[unique_msg_df['eval comment'].isin(['Y', 'N'])]

# Count occurrences of each value in 'eval comment'
eval_comment_counts = filtered_df['eval comment'].value_counts()

# Calculate percentage
eval_comment_percentage = eval_comment_counts / eval_comment_counts.sum() * 100

# Display the results
print("Count of 'Y' and 'N' in eval comment:")
print(eval_comment_counts)
print("\nPercentage of 'Y' and 'N' in eval comment:")
print(eval_comment_percentage)


# In[ ]:


# DataFrame for unique conv with >=2 msg



# In[68]:


import pandas as pd

# Assuming you already have unique_msg_df
# If not, replace 'your_file.csv' with the actual file path
# unique_msg_df = pd.read_csv('your_file.csv')

# Filter the DataFrame to include only 'Y' and 'N' values
filtered_df = unique_msg_df[unique_msg_df['eval comment'].isin(['Y', 'N'])]

# Count occurrences of each 'conv_id'
conv_id_counts = filtered_df['conv_id'].value_counts()

# Filter 'conv_id' with count equal to 2
selected_conv_ids = conv_id_counts[conv_id_counts >= 2].index

# Filter the DataFrame based on selected 'conv_id'
new_result_df = filtered_df[filtered_df['conv_id'].isin(selected_conv_ids)]

# Now, result_df contains rows where 'eval comment' is 'Y' or 'N' and 'conv_id' count is >=2


# In[69]:


new_result_df


# In[85]:


# Total count of coversation with >= 2 msg


new2_unique_conv_id_count = new_result_df['conv_id'].nunique()
new2_unique_conv_id_count


# In[98]:


# Count & Precentage -  of failure for conv with >=2 msg(having one or more N)


# Calculate the count of 'conv_id' having count >= 2 and "N" in eval comment
selected_conv_ids_df = new_result_df[new_result_df['eval comment'] == 'N']['conv_id'].value_counts()

# Calculate total count and percentage
total_count1 = selected_conv_ids_df.shape[0]
total_percentage = (total_count1 / new_result_df['conv_id'].nunique()) * 100

# Display the results
print(f"Total count of 'conv_id' having count >= 2 and 'N' in 'eval comment': {total_count1}")
print(f"Percentage: {total_percentage:.2f}%")


# In[93]:


# Count & Precentage -  of Success for conv with >=2 msg(having only Y)



# Calculate the count of 'conv_id' having count >= 2 and only "Y" in eval comment
Y_total_count=new2_unique_conv_id_count-total_count1

# Calculate total count and percentage
total_percentage = (Y_total_count / new_result_df['conv_id'].nunique()) * 100

# Display the results
print(f"Total count of 'conv_id' having count >= 2 and 'Y' in 'eval comment': {Y_total_count}")
print(f"Percentage: {total_percentage:.2f}%")


# In[ ]:





# In[ ]:





# In[ ]:




