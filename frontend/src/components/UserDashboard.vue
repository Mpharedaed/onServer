<template>
    <div>
      <h1>{{ message }}</h1>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        message: '',
      };
    },
    mounted() {
      const token = localStorage.getItem('token');
      fetch('/api/data', {
        headers: {
          'x-access-token': token
        }
      })
        .then(response => response.json())
        .then(data => {
          this.message = data.message;
        })
        .catch(error => {
          if (error.response && error.response.status === 403) {
            this.$router.push('/login');
          }
        });
    },
  };
  </script>
  