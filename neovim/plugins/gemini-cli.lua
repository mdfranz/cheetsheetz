return {
  "marcinjahn/gemini-cli.nvim",
  cmd = "Gemini", 
  keys = { 
    { "<leader>a/", "<cmd>Gemini toggle<cr>", desc = "Toggle Gemini CLI" }, 
    { "<leader>aa", "<cmd>Gemini ask<cr>", desc = "Ask Gemini", mode = { "n", "v" } }, 
    { "<leader>af", "<cmd>Gemini add_file<cr>", desc = "Add File" },
  },
  opts = {
    -- Command that executes Gemini CLI
    gemini_cmd = "gemini", 
    args = { }, 
    auto_reload = false, 
  }
}
