<template>
  <div class="invite-card">
    <div class="card-content">
      <h1 class="title">انضم إلى جلسات داولات المباشرة</h1>
      <p class="description">
        ندعوك للاشتراك في جلسات داولات المباشرة على فيسبوك. لا تفوت فرصة
        التفاعل المباشر مع داولات واستفد من خبرتها!
      </p>
      <a
        href="https://www.facebook.com/dody.reda.589"
        target="_blank"
        rel="noopener noreferrer"
        class="subscribe-button"
      >
        اشترك الآن
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "InviteCard",
};
</script>

<style scoped>
.invite-card {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #ff5f6d, #ffc371);
  direction: rtl; /* Ensure RTL for Arabic text */
  text-align: center;
}

.card-content {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
}

.title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.description {
  font-size: 1.25rem;
  margin-bottom: 1.5rem;
  color: #666;
}

.subscribe-button {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: #ff5f6d;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.subscribe-button:hover {
  background-color: #ff3e4d;
}
</style>
