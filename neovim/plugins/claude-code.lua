return {
  "greggh/claude-code.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim", -- Required by claude-code for git operations
  },
  cmd = "ClaudeCode",
  keys = {
    {
      "<leader>ac", 
      "<cmd>ClaudeCode<cr>", 
      desc = "Toggle Claude Code",
    },
  },
  opts = {
    -- The plugin works great out of the box, so we can leave this empty 
    -- to use the default settings, but the table must exist so AstroNvim
    -- knows to run the setup() function.
  },
}
