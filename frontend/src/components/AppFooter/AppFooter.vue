<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-logo">
          <h1>My App</h1>
        </div>
        <nav class="footer-navigation">
          <ul>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Terms of Service</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
        <div class="social-media">
          <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
          <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
          <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
        </div>
      </div>
      <p class="footer-copy">&copy; 2024 My App. All rights reserved.</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

.footer {
  background: linear-gradient(135deg, #4a4ae1, #6c63ff);
  color: white;
  padding: 40px 0 20px;
  text-align: center;
  box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.1);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}

.footer-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.footer-logo h1 {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
  margin: 0;
  font-size: 24px;
}

.footer-navigation ul {
  list-style: none;
  padding: 0;
  display: flex;
  gap: 20px;
  margin: 0;
}

.footer-navigation a {
  color: white;
  text-decoration: none;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
  transition: color 0.3s ease;
}

.footer-navigation a:hover {
  color: #e0e0e0;
}

.social-media a {
  color: white;
  margin: 0 10px;
  font-size: 20px;
  transition: color 0.3s ease, transform 0.3s ease;
}

.social-media a:hover {
  color: #e0e0e0;
  transform: scale(1.1);
}

.footer-copy {
  margin: 0;
  font-size: 14px;
  font-family: 'Roboto', sans-serif;
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
  }

  .footer-navigation ul {
    flex-direction: column;
    gap: 10px;
  }
}
</style>
