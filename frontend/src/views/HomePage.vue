<template>
  <div id="home">
    <!-- Navigation Dots -->
    <div class="navigation-dots">
      <span
        v-for="(section, index) in sections"
        :key="index"
        :class="{ active: currentSectionIndex === index }"
        @click="scrollToSection(index)"
      ></span>
    </div>

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

        <div class="scroll-indicator" @click="scrollToSection(2)">
          <span></span>
        </div>
      </section>

      <!-- Contact Section -->
      <section
        v-else-if="currentSectionIndex === 2"
        class="contact section"
        key="contact"
      >
        <div class="container">
          <h2 class="section-title">Get in Touch</h2>
          <p class="section-description">
            I'm here to help you on your journey. Feel free to reach out.
          </p>
          <!-- Contact form or information -->
          <!-- ... (Your contact content) ... -->
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
    let lastScrollTime = 0;
    const sections = ref(['hero', 'services', 'contact']);

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
        index >= sections.value.length ||
        index === currentSectionIndex.value
      ) {
        return;
      }

      transitionName.value =
        index > currentSectionIndex.value ? 'slide-up' : 'slide-down';
      currentSectionIndex.value = index;
    };

    // Wheel Event Handler with Throttle
    const handleWheel = (event) => {
      event.preventDefault();
      const now = Date.now();
      if (isAnimating.value || now - lastScrollTime < 800) return;

      lastScrollTime = now;
      const delta = event.deltaY;
      if (delta > 0) {
        scrollToSection(currentSectionIndex.value + 1);
      } else if (delta < 0) {
        scrollToSection(currentSectionIndex.value - 1);
      }
    };

    // Touch Event Handlers with Throttle
    const handleTouchStart = (event) => {
      touchStartY = event.touches[0].clientY;
    };

    const handleTouchEnd = (event) => {
      const touchEndY = event.changedTouches[0].clientY;
      const touchDelta = touchStartY - touchEndY;

      const now = Date.now();
      if (isAnimating.value || now - lastScrollTime < 800) return;

      lastScrollTime = now;

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
      sections,
    };
  },
};
</script>

<!-- Importing your CSS files -->
<style scoped>
@import '../../dist/css/hero.css';
@import '../../dist/css/global.css';
@import '../../dist/css/services.css';

</style>
