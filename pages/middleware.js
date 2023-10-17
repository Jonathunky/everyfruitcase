export { locales as middleware } from "nextra/locales"

let locales
if (typeof window !== "undefined") {
  locales = require("nextra/locales").locales
}
