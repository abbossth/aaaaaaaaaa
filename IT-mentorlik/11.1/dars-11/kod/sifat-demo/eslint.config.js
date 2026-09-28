import js from "@eslint/js";
import globals from "globals";

export default [
  js.configs.recommended,
  {
    languageOptions: { globals: { ...globals.node } },
    rules: {
      eqeqeq: "error",
      "no-unused-vars": "warn",
      "prefer-const": "error",
    },
  },
];
