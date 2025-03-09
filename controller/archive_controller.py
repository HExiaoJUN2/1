# controller/archive_controller.py
from model.db_init import SessionLocal
from model.archive import Archive

def create_archive(title, category, file_path=None):
    db = SessionLocal()
    try:
        new_archive = Archive(
            title=title,
            category=category,
            file_path=file_path
        )
        db.add(new_archive)
        db.commit()
        print("档案创建成功！")
        return new_archive
    except Exception as e:
        db.rollback()
        print("创建档案时出错：", e)
    finally:
        db.close()

def get_all_archives():
    db = SessionLocal()
    try:
        archives = db.query(Archive).all()
        return archives
    except Exception as e:
        print("查询档案时出错：", e)
        return []
    finally:
        db.close()

def delete_archive(archive_id):
    db = SessionLocal()
    try:
        archive = db.query(Archive).filter_by(id=archive_id).first()
        if archive:
            db.delete(archive)
            db.commit()
            print(f"档案 {archive_id} 已删除。")
        else:
            print(f"未找到id为 {archive_id} 的档案。")
    except Exception as e:
        db.rollback()
        print("删除档案时出错：", e)
    finally:
        db.close()
