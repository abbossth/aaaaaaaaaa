using System;
using RecipeManagementSystem.Services;
using Moq;
using RecipeManagementSystem.Models;

namespace MockSampleTest
{
    [TestClass]
    public class TestMoq
	{
        [TestMethod]
        public void TestRecipeAddMoq()
        {
            var ActionLogger = new Mock<ActionLogger>();
            RecipeService recipeService = new RecipeService(ActionLogger.Object);
            Recipe recipe = new Recipe();
            recipe.Name = "RecipeName";
            recipe.Description = "RecipeDescription";

            recipeService.Add(recipe);

            ActionLogger.Verify(
                logger => logger.LogActions("Add", recipe.Name), Times.Once);
        }

        [TestMethod] 
        public void TestRecipeUpdateMoq()
        {
            var ActionLogger = new Mock<ActionLogger>();
            RecipeService recipeService = new RecipeService(ActionLogger.Object);
            Recipe newRecipe = new Recipe();
            newRecipe.Name = "RecipeName (Update)";
            newRecipe.Description = "RecipeDescription (Update)";
            Guid lastRecipeId = recipeService.GetAll().Last().Id;

            recipeService.Update(lastRecipeId, newRecipe);

            ActionLogger.Verify(
                logger => logger.LogActions("Update", newRecipe.Name),
                Times.Once
            );
        }

        [TestMethod]
        public void TestDeleteMoq()
        {
            var ActionLogger = new Mock<ActionLogger>();
            RecipeService recipeService = new RecipeService(ActionLogger.Object);
            Recipe lastRecipe = recipeService.GetAll().Last();
            recipeService.Delete(lastRecipe.Id);
            ActionLogger.Verify(logger => logger.LogActions("Delete", lastRecipe.Name), Times.Once);
        }
    }
}
