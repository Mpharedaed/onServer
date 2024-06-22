<template>
  <div class="home">
    <h1>Home Page</h1>
    <p>Welcome to the Home page!</p>
    <div class="animated-text">
      <span>Xhelped</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  mounted() {
    const animatedText = document.querySelector('.animated-text span');
    window.addEventListener('mousemove', (e) => {
      const { clientX: x, clientY: y } = e;
      animatedText.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;
    });
  },
  beforeDestroy() {
    window.removeEventListener('mousemove', this.mouseMoveHandler);
  }
};
</script>

<style scoped>
.home {
  padding: 20px;
}

.animated-text {
  position: relative;
  font-size: 5rem;
  color: #6c63ff;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  overflow: hidden;
}

.animated-text span {
  display: inline-block;
  transition: transform 0.1s ease-out;
}
</style>
