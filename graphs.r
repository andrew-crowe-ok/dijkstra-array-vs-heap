# Install ggplot2 if you haven't already
if (!require(ggplot2)) install.packages("ggplot2")
library(ggplot2)

# 1. Load the benchmark data
# Make sure your working directory is set to where this CSV is located
df <- read.csv("benchmark_results.csv", stringsAsFactors = FALSE)

# Convert Vertices to numeric if it isn't already
df$Vertices <- as.numeric(df$Vertices)

# 2. Plot Time Complexity (Time vs. Vertices)
time_plot <- ggplot(df, aes(x = Vertices, y = Time_ms, color = Method, group = Method)) +
  geom_line(linewidth = 1) +
  geom_point(size = 3) +
  facet_wrap(~ Density, scales = "free_y") +
  theme_minimal() +
  labs(
    title = "Dijkstra's Algorithm: Execution Time",
    x = "Number of Vertices (V)",
    y = "Time (ms)",
    color = "Implementation"
  ) +
  theme(legend.position = "bottom")

# 3. Plot Space Complexity (Memory vs. Vertices)
memory_plot <- ggplot(df, aes(x = Vertices, y = Memory_MB, color = Method, group = Method)) +
  geom_line(linewidth = 1) +
  geom_point(size = 3) +
  facet_wrap(~ Density, scales = "free_y") +
  theme_minimal() +
  labs(
    title = "Dijkstra's Algorithm: Peak Memory Usage",
    x = "Number of Vertices (V)",
    y = "Memory (MB)",
    color = "Implementation"
  ) +
  theme(legend.position = "bottom")

# 4. Display the plots
print(time_plot)
print(memory_plot)

# 5. Save the plots for your report (Optional)
# ggsave("time_complexity_plot.png", plot = time_plot, width = 8, height = 5)
# ggsave("space_complexity_plot.png", plot = memory_plot, width = 8, height = 5)