<template>
  <div class="carousel">
    <section class="carosel_header">
      <section class="carousel_overlay" :class="{visible: isOverlayVisible}">
        <div v-html="activeFeature.title"></div>
      </section>
      <img class="carousel_image" :src="activeFeature.imageUrl" alt="">
    </section>
    <section class="carousel_description">
      <section class="carousel_slider-container">
        <div v-for="feature in features" @click="previewFeature(feature)" style="padding: 0.7rem 0.4rem">
          <div class="carousel_slider" :class="{active: feature === activeFeature}"></div>
        </div>
      </section>

      <div class="carousel_title" v-html="activeFeature.title"></div>
      <div class="carousel_detail" v-html="activeFeature.description"></div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOverlayVisible: false,
      overlayTimeout: null,
      interval: null,

      activeFeature: null,
      features: [
        {
          imageUrl: 'features/completions.gif',
          title: '<b>Smart auto complete</b>',
          description: 'Get smart code completion. Press <kbd>f12</kbd> to trigger the documentation popup.'
        },
        {
          imageUrl: 'features/diagnostics.gif',
          title: '<b>Diagnostics</b>',
          description: 'From the command palette select <code>LSP: Toggle Diagnostics Panel</code> to open the diagnostics panel. Use <kbd>F4</kbd> and <kbd>shift+f4</kbd> to go to the next/previous diagnostic.'
        },
        {
          imageUrl: 'features/definition.gif',
          title: '<b>Go to definition</b>',
          description: 'Go to symbol definition, type definition, declaration or implementation. '
        },
        {
          imageUrl: 'features/references.gif',
          title: '<b>Find references</b>',
          description: 'Find all symbol references across the project. Use <kbd>F4</kbd> and <kbd>shift+f4</kbd> to go to the next/previous reference.'
        },
        {
          imageUrl: 'features/rename.gif',
          title: '<b>Rename symbol</b>',
          description: 'Rename the symbol name accross the project.'
        },
        {
          imageUrl: 'features/highlight.gif',
          title: '<b>Document highlight</b>',
          description: '<u>Highlights</u> all references to the symbol scoped to the opened file.'
        },
        {
          imageUrl: 'features/code_actions.gif',
          title: '<b>Code actions</b>',
          description: 'Run commands to fix problems or to refactor code. Code actions can be triggered on save to automatically format your document or to organize imports.'
        },
      ]
    }
  },

  created() {
    this.previewFeature(this.features[0])
  },

  methods: {
    previewFeature(feature) {
      this.activeFeature = feature
      this.startCarousel()
      this.showOverlay()
    },

    showOverlay() {
        if (this.overlayTimeout) {
          clearTimeout(this.overlayTimeout)
        }

        this.isOverlayVisible = true
        this.overlayTimeout = setTimeout(() => {
          this.isOverlayVisible = false
        }, 2000)
    },

    startCarousel() {
      if (this.interval) {
        clearInterval(this.interval)
      }

      this.interval = setInterval(() => {
        const currentIndex = this.features.indexOf(this.activeFeature)

        // the % operator will make sure that the nextIndex is always in the range of 0-this.features.length
        const nextIndex = (currentIndex + 1) % this.features.length

        this.activeFeature = this.features[nextIndex]
        this.showOverlay()
      }, 17000)
    }
  }
}
</script>

<style scoped>
.carousel {
  width: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
  box-shadow: 0 4px 16px #00000040;
  border-radius: 8px;
  overflow: hidden;
}

.carosel_header {
  user-select: none;
  position: relative;
}

.carousel_image {
  display: flex;
  width: 100%;
  height: auto;
  margin: 0;
}

.carousel_overlay {
  display: flex;
  letter-spacing: 1.2px;
  font-family: "Lucida Console", Monaco, monospace;
  align-items: center;
  justify-content: center;
  position: absolute;
  text-transform: uppercase;
  width: 100%;
  height: 100%;
  background: #00000077;
  color: #fff;
  font-size: 20px;
  transition: opacity 0.3s;
  opacity: 0;
}

.carousel_overlay.visible {
  opacity: 1;
}

.carousel_description {
  position: relative;
  padding: 1rem 2rem;
  min-height: 100px;
  background: #00000020;
  width: 100%;
}

.dark-mode .carousel_description {
  background: #00000050;
}

.carousel_slider-container {
  display: flex;
  justify-content: center;
  position: absolute;
  left: 0;
  top: -30px;
  width: 100%;
}

.carousel_slider {
  background: #00000030;
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 4px;
}


.carousel_slider.active {
  background: #ffb833;
}

.carousel_title {
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.carousel_detail {
  line-height: 20px;
}
</style>
