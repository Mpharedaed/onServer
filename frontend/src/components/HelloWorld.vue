<!-- src/components/HelloWorld.vue -->
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
    fetch('/api/data')
      .then(response => response.json())
      .then(data => {
        this.message = data.message;
      });
  },
};
</script>
