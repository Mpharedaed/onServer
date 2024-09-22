<template>
  <div id="home">
    <!-- Transition Wrapper -->
    <transition
      :name="transitionName"
      mode="out-in"
      @before-enter="beforeEnter"
      @after-enter="afterEnter"
    >
      <!-- Hero Section -->
      <section
        v-if="currentSectionIndex === 0"
        class="hero section"
        key="hero"
      >
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
              Join me, Dawlat Emad, on a transformative journey towards
              self-discovery and personal growth.
            </p>
            <button class="hero-button" @click="openStory">My Story</button>
            <button class="hero-button" @click="openContact">
              Contact Me
            </button>
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

      <!-- Services Section -->
      <section
        v-else-if="currentSectionIndex === 1"
        class="services section"
        key="services"
      >
        <div class="container">
          <h2 class="section-title">Our Services</h2>
          <p class="section-description">
            Explore the services we offer to help you on your journey towards
            personal growth and self-discovery.
          </p>

          <div class="services-grid">
            <!-- Service 1 -->
            <div class="service-item">
              <img
                src="path-to-icon1.png"
                alt="Service 1 Icon"
                class="service-icon"
              />
              <h3 class="service-title">Life Coaching</h3>
              <p class="service-description">
                Personalized one-on-one coaching sessions designed to help you
                discover your potential and set actionable goals for success.
              </p>
            </div>

            <!-- Service 2 -->
            <div class="service-item">
              <img
                src="path-to-icon2.png"
                alt="Service 2 Icon"
                class="service-icon"
              />
              <h3 class="service-title">Mindfulness Training</h3>
              <p class="service-description">
                Learn techniques to enhance your mindfulness and reduce stress
                through guided meditation and practical exercises.
              </p>
            </div>

            <!-- Service 3 -->
            <div class="service-item">
              <img
                src="path-to-icon3.png"
                alt="Service 3 Icon"
                class="service-icon"
              />
              <h3 class="service-title">Workshops & Seminars</h3>
              <p class="service-description">
                Participate in group workshops and seminars focused on
                self-improvement, leadership, and emotional resilience.
              </p>
            </div>
          </div>
        </div>

        <div class="scroll-indicator" @click="scrollToSection(0)">
          <span></span>
        </div>
      </section>
    </transition>

    <!-- Modals -->
    <StoryModal :showStory="showStory" @close="closeStory" />
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
    const currentSectionIndex = ref(0);
    const transitionName = ref('slide-up');
    const isAnimating = ref(false);
    let touchStartY = 0;

    const sectionsCount = 2; // Update this if you add more sections

    // Open and Close Modals
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

    // Scroll to Section Function
    const scrollToSection = (index) => {
      if (
        isAnimating.value ||
        index < 0 ||
        index >= sectionsCount ||
        index === currentSectionIndex.value
      ) {
        return;
      }

      transitionName.value =
        index > currentSectionIndex.value ? 'slide-up' : 'slide-down';
      currentSectionIndex.value = index;
    };

    // Wheel Event Handler
    const handleWheel = (event) => {
      event.preventDefault();
      if (isAnimating.value) return;

      const delta = event.deltaY;
      if (delta > 0) {
        scrollToSection(currentSectionIndex.value + 1);
      } else if (delta < 0) {
        scrollToSection(currentSectionIndex.value - 1);
      }
    };

    // Touch Event Handlers
    const handleTouchStart = (event) => {
      touchStartY = event.touches[0].clientY;
    };

    const handleTouchEnd = (event) => {
      const touchEndY = event.changedTouches[0].clientY;
      const touchDelta = touchStartY - touchEndY;

      if (isAnimating.value) return;

      if (touchDelta > 50) {
        scrollToSection(currentSectionIndex.value + 1);
      } else if (touchDelta < -50) {
        scrollToSection(currentSectionIndex.value - 1);
      }
    };

    // Animation Control
    const beforeEnter = () => {
      isAnimating.value = true;
    };

    const afterEnter = () => {
      isAnimating.value = false;
    };

    // Lifecycle Hooks
    onMounted(() => {
      window.addEventListener('wheel', handleWheel, { passive: false });
      window.addEventListener('touchstart', handleTouchStart, {
        passive: false,
      });
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
      currentSectionIndex,
      scrollToSection,
      transitionName,
      beforeEnter,
      afterEnter,
    };
  },
};
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

/* Reset and General Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Montserrat', sans-serif;
  overflow: hidden; /* Prevent default scrolling */
}

#home {
  height: 100vh;
  overflow: hidden;
}

/* Sections */
.section {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

/* Transition Styles */
.slide-up-enter-active,
.slide-up-leave-active,
.slide-down-enter-active,
.slide-down-leave-active {
  transition: transform 0.8s ease, opacity 0.8s ease;
}

.slide-up-enter-from,
.slide-up-leave-to {
  transform: translateY(100%);
  opacity: 0;
}

.slide-up-enter-to,
.slide-up-leave-from {
  transform: translateY(0);
  opacity: 1;
}

.slide-down-enter-from,
.slide-down-leave-to {
  transform: translateY(-100%);
  opacity: 0;
}

.slide-down-enter-to,
.slide-down-leave-from {
  transform: translateY(0);
  opacity: 1;
}

/* Hero Section */
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #fff;
}

/* Hero Background */
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
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

/* Adjust layers as needed */
.layer-1 {
  background-image: url('@/assets/images/layer1.png');
  z-index: 1;
}

.layer-2 {
  background-image: url('@/assets/images/layer2.png');
  z-index: 2;
  opacity: 0.5;
}

.layer-3 {
  background-image: url('@/assets/images/layer3.png');
  z-index: 3;
  opacity: 0.3;
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

.color-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(60, 64, 239, 0.3);
  z-index: 5;
  backdrop-filter: blur(10px);
}

/* Hero Content */
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
  margin: 0 10px;
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

/* Scroll Indicator */
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

/* Services Section */
.services {
  background-color: #f9f9f9;
  padding: 4rem 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.services .container {
  text-align: center;
  max-width: 1200px;
}

.section-title {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.section-description {
  font-size: 1.2rem;
  margin-bottom: 3rem;
  color: #666;
}

/* Services Grid Layout */
.services-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.service-item {
  flex: 0 1 30%; /* Adjust as needed */
  text-align: center;
  padding: 1.5rem;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-item:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.service-icon {
  width: 60px;
  height: 60px;
  margin-bottom: 1rem;
}

.service-title {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.service-description {
  font-size: 1rem;
  color: #666;
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

  .services-grid {
    flex-direction: column;
    align-items: center;
  }

  .service-item {
    flex: 0 1 80%;
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

  .scroll-indicator span {
    width: 20px;
    height: 20px;
  }

  .service-item {
    flex: 0 1 100%;
  }
}
</style>
