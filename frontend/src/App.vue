<template>
  <div id="app">
    <AppHeader />
    <main>
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue';
import AppFooter from '@/components/AppFooter.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter
  }
};
</script>

<style>
body, html, #app {
  margin: 0;
  padding: 0;
  height: 100%;
}

main {
  padding: 20px;
  min-height: calc(100vh - 120px); /* Adjust based on header and footer height */
  box-sizing: border-box;
}
</style>
