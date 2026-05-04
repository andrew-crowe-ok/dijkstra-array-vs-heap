library(ggplot2)

# Ensure that csv is in working directory
data <- read.csv("benchmark_results.csv", header=TRUE)

# Cleaner x-axis labels
data$Vertices <- data$Vertices / 1000

# Set graph order to Sparse -> Medium -> Dense
data$Density <- factor(data$Density, levels = c("Sparse", "Medium", "Dense"))

# Define theme
my_theme <- theme_minimal(base_size = 16) +
  theme(
    plot.title = element_text(face = "bold", size = 18, hjust = 0.5, margin = margin(b = 20)),
    strip.text = element_text(face = "bold", size = 14, color = "#333333"),
    strip.background = element_rect(fill = "#F5F5F5", color = NA),
    legend.position = "bottom",
    legend.title = element_text(face = "bold", size = 14),
    legend.text = element_text(face = "bold", size = 12),
    
    # Emphasize horizontal grid lines to highlight shared y-axis
    panel.grid.major.y = element_line(color = "#C0C0C0", linewidth = 0.8),
    panel.grid.major.x = element_line(color = "#E0E0E0", linewidth = 0.6),
    panel.grid.minor = element_blank(), 
    
    panel.border = element_rect(color = "#CCCCCC", fill = NA, linewidth = 0.8),
    axis.text = element_text(face = "bold", size = 12, color = "#555555"),
    axis.title.x = element_text(margin = margin(t = 15), face = "bold", size = 14, color = "#333333"),
    axis.title.y = element_text(margin = margin(r = 15), face = "bold", size = 14, color = "#333333"),
    plot.margin = margin(t = 30, r = 30, b = 30, l = 30)
  )
my_colors <- scale_color_manual(values = c("#2A9D8F", "#E76F51", "#264653"))

# Plot time complexity
time_plot <- ggplot(data, aes(x = Vertices, y = Time_ms, color = Method, group = Method)) +
  geom_line(linewidth = 1.4, alpha = 0.8) + 
  geom_point(size = 3.5, alpha = 0.9) +    
  facet_wrap(~ Density) + 
  my_colors +
  my_theme +
  labs(
    title = "Dijkstra's Algorithm: Execution Time",
    x = "Number of Vertices (V, in thousands)",
    y = "Time (ms)",
    color = "Implementation"
  )

# Plot space complexity
memory_plot <- ggplot(data, aes(x = Vertices, y = Memory_MB, color = Method, group = Method)) +
  geom_line(linewidth = 1.4, alpha = 0.8) +
  geom_point(size = 3.5, alpha = 0.9) +  
  facet_wrap(~ Density, scales = "free_y") + 
  my_colors +
  my_theme +
  labs(
    title = "Dijkstra's Algorithm: Peak Memory Usage",
    x = "Number of Vertices (V, in thousands)",
    y = "Memory (MB)",
    color = "Implementation"
  )

print(memory_plot)
print(time_plot)

ggsave("time_complexity_plot.png", plot = time_plot, width = 10, height = 6, dpi = 300, bg = "white")
ggsave("space_complexity_plot.png", plot = memory_plot, width = 10, height = 6, dpi = 300, bg = "white")