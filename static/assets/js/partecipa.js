document.addEventListener("alpine:init", () => {
  Alpine.data("modal_partecipa", () => ({
    loading: true,
    step: -1,
    titoEvent: "",
    event: null,

    async init() {
      this.loading = true;
      try {
        const res = await fetch("https://checkout.tito.io/coderdojovr.json");
        if (res.ok) {
          const data = await res.json();
          if (data.events && data.events.upcoming && data.events.upcoming.length > 0) {
            this.event = data.events.upcoming[0];
            if (this.event.url) {
              this.titoEvent = this.event.url.replace(/^https?:\/\/(www\.)?ti\.to\//, "");
            }
            this.step = 0;
          } else {
            this.step = -1;
          }
        } else {
          this.step = -1;
        }
      } catch (e) {
        console.error("Error loading Tito events:", e);
        this.step = -1;
      } finally {
        this.loading = false;
      }
    },

    resetStep() {
      this.step = this.titoEvent ? 0 : -1;
    },

    finish() {
      this.$refs.modal_partecipa.close();
      this.resetStep();
    },
  }));
});
