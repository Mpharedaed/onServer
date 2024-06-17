<template>
  <div class="data-container">
    <h1>{{ message }}</h1>
    <ul class="data-list">
      <li v-for="item in data" :key="item">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '',
      data: []
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/data');
        this.message = response.data.message;
        this.data = response.data.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  }
};
</script>

<style scoped>
.data-container {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 5px;
  max-width: 600px;
  margin: 0 auto;
}

h1 {
  font-size: 24px;
  color: #333;
}

.data-list {
  list-style-type: none;
  padding: 0;
}

.data-list li {
  background-color: #fff;
  margin: 5px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 3px;
  transition: background-color 0.3s;
}

.data-list li:hover {
  background-color: #f1f1f1;
}
</style>
