<template>
  <div id="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-background">
        <!-- Parallax Background Layers -->
        <div class="parallax-layer layer-1"></div>
        <div class="parallax-layer layer-2"></div>
        <div class="parallax-layer layer-3"></div>
        <!-- Overlay for gradient or color tint -->
        <div class="background-overlay"></div>
      </div>
      <div class="container hero-container">
        <div class="hero-content">
          <h1 class="hero-title">Discover Your True Potential</h1>
          <p class="hero-subtitle">
            Join me, Dawlat Emad, on a transformative journey towards self-discovery and personal growth.
          </p>
          <button class="hero-button" @click="openStory">My Story</button>
        </div>
        <div class="hero-image-wrapper">
          <img
            src="@/assets/images/dawlat.png"
            alt="Dawlat Emad"
            class="hero-image"
          />
        </div>
      </div>
      <div class="scroll-indicator" @click="scrollToContent">
        <span></span>
      </div>
    </section>

    <!-- Story Modal -->
    <div v-if="showStory" class="story-widget" @click.self="closeStory">
      <div class="story-content rtl">
        <button class="close-button" @click="closeStory">&times;</button>
        <h2 class="story-title">About Dawlat Emad</h2>
        <p class="story-text">
          دولت عماد هي كوتش حياة شغوفة، مخصصة إنها تساعد الناس يكتشفوا إمكانياتهم الحقيقية ويحققوا أحلامهم. بأسلوب بسيط وجميل بيجمع بين التعاطف والخبرة، دولت بتمكن عملاءها من تجاوز التحديات واكتشاف قوتهم الداخلية.
        </p>
        <h3 class="story-subheading">تخصصات دولت تشمل:</h3>
        <ul class="story-list">
          <li><strong>بناء الثقة:</strong> بتساعد السيدات يستعيدوا قوتهم وصوتهم في الحياة الشخصية والمهنية.</li>
          <li><strong>الكوتشينج المهني:</strong> بترشد الأفراد في تحديد أهدافهم المهنية وتوجيه حياتهم العملية ناحية شغفهم.</li>
          <li><strong>الصحة النفسية:</strong> بتدعم عملاءها في إدارة التوتر والقلق وتعدي المراحل الصعبة في حياتهم بأساليب مخصصة للمرونة النفسية.</li>
          <li><strong>تطوير القيادة:</strong> بتمكن السيدات والقادة الجدد إنهم يمسكوا مناصب قيادية بشجاعة وثقة.</li>
        </ul>
        <p class="story-text">
          دولت معروفة بأسلوبها الدافئ والداعم. بتقدم مش بس أدوات عملية، لكن كمان بتدي الدعم النفسي اللي عملاءها بيحتاجوه عشان يحققوا النجاح.
        </p>
        <!-- Call-to-action button -->
        <a href="#contact" class="story-button">ابدأ رحلتك الآن</a>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, onMounted } from 'vue';

export default {
  name: 'HomePage',
  setup() {
    const showStory = ref(false);

    const openStory = () => {
      showStory.value = true;
      document.body.style.overflow = 'hidden';
    };

    const closeStory = () => {
      showStory.value = false;
      document.body.style.overflow = 'auto';
    };

    const scrollToContent = () => {
      const nextSection = document.querySelector('.services');
      if (nextSection) {
        nextSection.scrollIntoView({ behavior: 'smooth' });
      }
    };

    // Parallax Effect

const handleParallax = () => {
  const layers = document.querySelectorAll('.parallax-layer');
  window.addEventListener('scroll', () => {
    const scrollPosition = window.pageYOffset;
    layers.forEach((layer) => { // Remove 'index' as it's unused
      const speed = layer.getAttribute('data-speed');
      layer.style.transform = `translateY(${scrollPosition * speed}px)`;
    });
  });
};


    onMounted(() => {
      handleParallax();
    });

    return {
      showStory,
      openStory,
      closeStory,
      scrollToContent,
    };
  },
};
</script>
<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Cairo:wght@400;600;700&display=swap');

/* Reset and General Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Open Sans', sans-serif;
  background-color: #f9f9f9;
  overflow-x: hidden;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  cursor: pointer;
  border: none;
  outline: none;
}

/* Hero Section */
.hero {
  position: relative;
  height: 100vh;
  color: #fff;
  overflow: hidden;
  perspective: 1px;
  transform-style: preserve-3d;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  overflow: hidden;
}

.parallax-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}


.layer-2 {
  background-image: url('@/assets/images/layer2.png');
  z-index: 2;
  opacity: 0.5;
  data-speed: 0.4;
}

.layer-3 {
  background-image: url('@/assets/images/layer2video.mp4 ');
  z-index: 3;
  opacity: 0.3;
  data-speed: 0.6;
}





.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to bottom right,
    rgba(0, 0, 0, 0.6),
    rgba(0, 0, 0, 0.3)
  );
  z-index: 4;
}

.hero-container {
  position: relative;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  padding: 0 5%;
}

.hero-content {
  flex: 1;
  animation: fadeInLeft 1s forwards;
}

.hero-title {
  font-size: 3.5rem;
  margin-bottom: 1rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  text-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  line-height: 1.5;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.hero-button {
  background-color: rgba(255, 255, 255, 0.2);
  color: #fff;
  padding: 1rem 2rem;
  border-radius: 50px;
  font-size: 1.2rem;
  transition: background-color 0.3s ease;
  border: 1px solid #fff;
  backdrop-filter: blur(5px);
}

.hero-button:hover {
  background-color: rgba(255, 255, 255, 0.4);
}

.hero-image-wrapper {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  animation: fadeInRight 1s forwards;
  position: relative;
}

.hero-image {
  border-radius: 50%;
  width: 400px;
  height: 400px;
  object-fit: cover;
  border: 5px solid rgba(255, 255, 255, 0.5);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(5px);
}

.hero-image::after {
  content: '';
  position: absolute;
  top: -20px;
  right: -20px;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 2px dashed rgba(255, 255, 255, 0.5);
}

.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  cursor: pointer;
}

.scroll-indicator span {
  display: block;
  width: 30px;
  height: 30px;
  border-bottom: 3px solid #fff;
  border-right: 3px solid #fff;
  transform: rotate(45deg);
  animation: scrollDown 2s infinite;
}

/* Story Widget Styles */
.story-widget {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(10px);
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.6s forwards;
}

.story-content {
  backdrop-filter: blur(20px);
  background: rgba(255, 255, 255, 0.7);
  width: 90%;
  max-width: 800px;
  padding: 2rem 3rem;
  border-radius: 20px;
  position: relative;
  overflow-y: auto;
  animation: zoomIn 0.5s forwards;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.close-button {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: none;
  border: none;
  font-size: 2rem;
  color: #555;
  cursor: pointer;
  z-index: 1100; /* Ensure it's on top of the modal content */
  padding: 10px; /* Increase clickable area */
  transition: color 0.3s ease;
}

.close-button:hover {
  color: #ff6f61;
}

@media (max-width: 768px) {
  .close-button {
    top: 1rem;
    right: 1rem; /* Adjust the position for small screens */
    font-size: 1.8rem;
    padding: 15px; /* Larger tap area for better mobile experience */
  }
}

.story-title {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-family: 'Cairo', sans-serif;
  font-weight: 700;
  color: #333;
  position: relative;
}

.story-title::after {
  content: '';
  width: 80px;
  height: 4px;
  background: linear-gradient(90deg, #ff6f61, #e65b50);
  position: absolute;
  left: 0;
  bottom: -10px;
  border-radius: 2px;
}

.story-text {
  font-size: 1.2rem;
  line-height: 1.8;
  color: #555;
  margin-bottom: 2rem;
  font-family: 'Cairo', sans-serif;
}

.story-subheading {
  font-size: 1.8rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: #333;
  font-family: 'Cairo', sans-serif;
  font-weight: 600;
}

.story-list {
  list-style: none;
  padding: 0;
  margin-bottom: 2rem;
}

.story-list li {
  font-size: 1.2rem;
  line-height: 1.8;
  margin-bottom: 1rem;
  position: relative;
  padding-left: 1.5rem;
  font-family: 'Cairo', sans-serif;
}

.story-list li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: #ff6f61;
  font-size: 1.5rem;
}

.story-button {
  background-color: #ff6f61;
  color: #fff;
  padding: 1rem 2.5rem;
  border-radius: 50px;
  font-size: 1.1rem;
  transition: background-color 0.3s ease;
  text-decoration: none;
  display: inline-block;
}

.story-button:hover {
  background-color: #e65b50;
}

.rtl {
  direction: rtl;
  text-align: right;
}

.rtl .close-button {
  left: 1.5rem;
  right: unset;
}

.rtl .story-title::after {
  left: unset;
  right: 0;
}

.rtl .story-list li {
  padding-left: 0;
  padding-right: 1.5rem;
}

.rtl .story-list li::before {
  left: unset;
  right: 0;
}

/* Animations */
@keyframes scrollDown {
  0% {
    transform: translateX(-50%) rotate(45deg) translateY(0);
    opacity: 1;
  }
  100% {
    transform: translateX(-50%) rotate(45deg) translateY(15px);
    opacity: 0;
  }
}

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInRight {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes zoomIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Responsive Design */
@media (max-width: 992px) {
  .hero-container {
    flex-direction: column;
    padding: 0 2rem;
    text-align: center;
  }

  .hero-content {
    animation: fadeInUp 1s forwards;
    order: 2;
  }

  .hero-image-wrapper {
    margin-bottom: 2rem;
    animation: fadeInUp 1s forwards;
    order: 1;
  }

  .hero-title {
    font-size: 3rem;
  }

  .hero-subtitle {
    font-size: 1.2rem;
  }

  .hero-image {
    width: 300px;
    height: 300px;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .hero-image {
    width: 250px;
    height: 250px;
  }

  .story-content {
    padding: 1.5rem 1.5rem;
  }

  .close-button {
    top: 1rem;
    left: 1rem;
  }

  .story-title {
    font-size: 2rem;
  }

  .story-text {
    font-size: 1rem;
  }
}
</style>
