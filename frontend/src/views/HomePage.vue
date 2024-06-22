<template>
  <div class="home">
    <aside class="sidebar">
      <h1>XHELPED</h1>
      <p>THANK YOU!!!</p>
    </aside>
    <main class="main-content">
      <div class="post" v-for="(post, index) in posts" :key="index">
        <div class="post-header">
          <img :src="post.avatar" alt="Avatar" class="avatar" />
          <div class="post-info">
            <h2>{{ post.name }}</h2>
          </div>
        </div>
        <div class="post-body">
          <p>{{ post.content }}</p>
        </div>
        <div class="post-footer">
          <span class="icon">&#9829;</span>
          <span class="icon">&#128172;</span>
          <span class="icon">&#9733;</span>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      posts: [
        {
          name: 'AYA',
          avatar: 'https://via.placeholder.com/50',
          content: 'Lorem ipsum is simply dummy text of the printing and typesetting industry...'
        },
        {
          name: 'AYA',
          avatar: 'https://via.placeholder.com/50',
          content: 'Lorem ipsum is simply dummy text of the printing and typesetting industry...'
        },
        {
          name: 'AYA',
          avatar: 'https://via.placeholder.com/50',
          content: 'Lorem ipsum is simply dummy text of the printing and typesetting industry...'
        }
      ]
    };
  }
};
</script>

<style scoped>
.home {
  display: flex;
  height: 100vh;
  font-family: 'Roboto', sans-serif;
}

.sidebar {
  background-color: #4c3b4d;
  color: white;
  width: 20%;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sidebar h1 {
  margin-bottom: 50px;
}

.sidebar p {
  font-size: 1.5em;
}

.main-content {
  background-color: #f0f0f0;
  width: 80%;
  padding: 20px;
  overflow-y: auto;
}

.post {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  padding: 20px;
}

.post-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 20px;
}

.post-info h2 {
  margin: 0;
}

.post-body p {
  margin: 0;
}

.post-footer {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.icon {
  font-size: 1.5em;
  cursor: pointer;
}
</style>
