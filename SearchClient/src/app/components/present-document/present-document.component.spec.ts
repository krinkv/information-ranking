import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PresentDocumentComponent } from './present-document.component';

describe('PresentDocumentComponent', () => {
  let component: PresentDocumentComponent;
  let fixture: ComponentFixture<PresentDocumentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [PresentDocumentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PresentDocumentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
