<template>
  <div id="home">
    <!-- Hero Section -->
    <section class="hero section">
      <!-- Hero content -->
      <div class="hero-background">
        <!-- Parallax Background Layers -->
        <div class="parallax-layer layer-1"></div>
        <div class="parallax-layer layer-2"></div>
        <div class="parallax-layer layer-3"></div>
        <div class="background-overlay"></div>
        <div class="color-overlay"></div>
      </div>
      <div class="container hero-container">
        <div class="hero-content">
          <h1 class="hero-title">Discover Your True Potential</h1>
          <p class="hero-subtitle">
            Join me, Dawlat Emad, on a transformative journey towards self-discovery and personal growth.
          </p>
          <button class="hero-button" @click="openStory">My Story</button>
          <button class="hero-button" @click="openContact">Contact Me</button>
        </div>
        <div class="hero-image-wrapper">
          <img
            src="@/assets/images/dawlat.png"
            alt="Dawlat Emad"
            class="hero-image"
          />
        </div>
      </div>
      <div class="scroll-indicator" @click="scrollToSection(1)">
        <span></span>
      </div>
    </section>

    <!-- New Section: Services -->
    <section class="services section">
      <div class="container">
        <h2 class="section-title">Our Services</h2>
        <p class="section-description">
          Explore the services we offer to help you on your journey.
        </p>
        <!-- Add your services content here -->
      </div>
      <div class="scroll-indicator" @click="scrollToSection(0)">
        <span></span>
      </div>
    </section>

    <!-- Use the StoryModal component -->
    <StoryModal :showStory="showStory" @close="closeStory" />

    <!-- Use the ContactModal component -->
    <ContactModal :showContact="showContact" @close="closeContact" />
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import StoryModal from '@/components/StoryModal.vue';
import ContactModal from '@/components/ContactModal.vue';

export default {
  name: 'HomePage',
  components: {
    StoryModal,
    ContactModal,
  },
  setup() {
    const showStory = ref(false);
    const showContact = ref(false);
    const sections = ref([]);
    const currentSectionIndex = ref(0);
    const isAnimating = ref(false);
    const touchStartY = ref(0);

    const openStory = () => {
      showStory.value = true;
      document.body.style.overflow = 'hidden';
    };

    const closeStory = () => {
      showStory.value = false;
      document.body.style.overflow = 'auto';
    };

    const openContact = () => {
      showContact.value = true;
      document.body.style.overflow = 'hidden';
    };

    const closeContact = () => {
      showContact.value = false;
      document.body.style.overflow = 'auto';
    };

    const scrollToSection = (index) => {
      if (
        isAnimating.value ||
        index < 0 ||
        index >= sections.value.length ||
        index === currentSectionIndex.value
      ) {
        return;
      }

      isAnimating.value = true;
      const direction = index > currentSectionIndex.value ? 'down' : 'up';

      const currentSection = sections.value[currentSectionIndex.value];
      const nextSection = sections.value[index];

      currentSection.classList.add('transition-out', direction);
      nextSection.style.display = 'block'; // Ensure the next section is visible
      nextSection.classList.add('transition-in', direction);

      currentSectionIndex.value = index;

      setTimeout(() => {
        currentSection.classList.remove('transition-out', direction);
        currentSection.style.display = 'none';
        nextSection.classList.remove('transition-in', direction);
        isAnimating.value = false;
      }, 1000); // Match this duration with CSS animation duration
    };

    const handleWheel = (event) => {
      event.preventDefault();
      if (isAnimating.value) return;

      const delta = event.deltaY;
      if (delta > 0) {
        // Scroll down
        scrollToSection(currentSectionIndex.value + 1);
      } else if (delta < 0) {
        // Scroll up
        scrollToSection(currentSectionIndex.value - 1);
      }
    };

    const handleTouchStart = (event) => {
      touchStartY.value = event.touches[0].clientY;
    };

    const handleTouchEnd = (event) => {
      const touchEndY = event.changedTouches[0].clientY;
      const touchDelta = touchStartY.value - touchEndY;

      if (isAnimating.value) return;

      if (touchDelta > 50) {
        // Swipe up
        scrollToSection(currentSectionIndex.value + 1);
      } else if (touchDelta < -50) {
        // Swipe down
        scrollToSection(currentSectionIndex.value - 1);
      }
    };

    onMounted(() => {
      sections.value = document.querySelectorAll('.section');
      sections.value.forEach((section, index) => {
        if (index !== 0) {
          section.style.display = 'none';
        }
      });

      window.addEventListener('wheel', handleWheel, { passive: false });
      window.addEventListener('touchstart', handleTouchStart, { passive: false });
      window.addEventListener('touchend', handleTouchEnd, { passive: false });
    });

    onBeforeUnmount(() => {
      window.removeEventListener('wheel', handleWheel);
      window.removeEventListener('touchstart', handleTouchStart);
      window.removeEventListener('touchend', handleTouchEnd);
    });

    return {
      showStory,
      openStory,
      closeStory,
      showContact,
      openContact,
      closeContact,
      scrollToSection,
    };
  },
};
</script>




<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Cairo:wght@400;600;700&display=swap');


/* Hero Section and General Styles */
.hero-button {
  background-color: rgba(255, 255, 255, 0.2);
  color: #fff;
  padding: 1rem 2rem;
  border-radius: 50px;
  font-size: 1.2rem;
  margin: 0 10px; /* Space between buttons */
  transition: background-color 0.3s ease;
  border: 1px solid #fff;
  backdrop-filter: blur(5px);
}

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
  background-image: url('@/assets/images/layer2video.mp4');
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
  background: linear-gradient(to bottom right, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.3));
  z-index: 4;
}

.color-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(60, 64, 239, 0.3); /* Color overlay with opacity */
  z-index: 5;
  backdrop-filter: blur(10px);
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

/* Additional Styling for Blurring and Transitions */
.text-background {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  padding: 1rem;
  border-radius: 10px;
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

/* Responsive Adjustments */
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
