using System.ComponentModel.DataAnnotations;

namespace WebApplication1.Models
{
    public class Order
    {
        [Key]
        public int Id_or { get; set; }
        public string Name_or { get; set; }

        public DateTime OrderDate { get; set; }
    }
}
