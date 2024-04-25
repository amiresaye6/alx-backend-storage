-- Context: Updating multiple tables for one action from your application can generate issue:
--  network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

CREATE TRIGGER sub_item
    AFTER INSERT ON orders
    FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
