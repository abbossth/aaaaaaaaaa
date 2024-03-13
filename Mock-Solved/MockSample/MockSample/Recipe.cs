using System;

namespace RecipeManagementSystem.Models
{
    public class Recipe
    {
        public Guid Id { get; set; } = Guid.NewGuid();
        public string Name { get; set; }
        public string Description { get; set; }
        // Add other properties as needed
    }
}
