document.addEventListener("alpine:init", () => {
  Alpine.data("dates", () => ({
    today: new Date(),
    coming_dates: [],
    past_dates: [],

    load_dates(dates) {
      this.today.setUTCHours(0, 0, 0, 0);

      for (const date_txt of dates.slice(1, -1).split(", ")) {
        const date = new Date(date_txt);
        if (date < this.today)
          this.past_dates = this.past_dates.concat(date);
        else
          this.coming_dates = this.coming_dates.concat(date);
      }
    },
  }))
})
